import sqlite3
from datetime import datetime
import os

#  AUTO YEAR DATABASE 
year = datetime.now().year
base_path = os.path.dirname(os.path.abspath(__file__))
db_name = os.path.join(base_path, f"electricity_{year}.db")

conn = sqlite3.connect(db_name)
cursor = conn.cursor()

#  Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS bills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT,
    month TEXT,
    year INTEGER,
    start_unit INTEGER,
    end_unit INTEGER,
    total_unit INTEGER,
    amount INTEGER,
    created_at TEXT,
    UNIQUE(phone, month, year)
)
""")
conn.commit()


def calculate_bill(start, end):
    total = end - start
    if total <= 50:
        amount = total * 5
    else:
        amount = 50 * 5 + (total - 50) * 10
    return total, amount


#  ALL MONTHS
months = [
    "January","February","March","April",
    "May","June","July","August",
    "September","October","November","December"
]

name = input("Enter Name: ")
phone = input("Enter Phone: ")
month = input("Enter Month: ")

if month not in months:
    print(" Invalid Month")
    exit()

# =====================================================
#  CHECK EXISTING BILL
# =====================================================
cursor.execute("""
SELECT * FROM bills 
WHERE phone=? AND month=? AND year=?
""", (phone, month, year))

existing = cursor.fetchone()

if existing:
    print("\n" + "="*45)
    print("       ELECTRICITY BILL RECEIPT")
    print("="*45)

    print(f"Name        : {existing[1]}")
    print(f"Phone       : {existing[2]}")
    print(f"Month       : {existing[3]}")

    print("-"*45)
    print(f"{'Start Unit':<20}: {existing[5]}")
    print(f"{'End Unit':<20}: {existing[6]}")
    print(f"{'Units Used':<20}: {existing[7]}")
    print("-"*45)

    print(f"{'Total Amount':<20}: ₹ {existing[8]}")
    print("-"*45)
    print(f"{' Paid On':<20}: {existing[9]}")

    print("="*45)
    print("    PAYMENT ALREADY DONE")
    print("="*45)

    conn.close()
    exit()

# =====================================================
#  NEW BILL LOGIC
# =====================================================
month_index = months.index(month)

#  JANUARY (CROSS YEAR)
if month == "January":
    prev_year = year - 1
    prev_db = os.path.join(base_path, f"electricity_{prev_year}.db")

    start_unit = 0  # default

    try:
        conn_prev = sqlite3.connect(prev_db)
        cursor_prev = conn_prev.cursor()

        cursor_prev.execute("""
        SELECT end_unit FROM bills 
        WHERE phone=? AND month='December'
        """, (phone,))

        result = cursor_prev.fetchone()

        if result:
            start_unit = result[0]   #  carry forward

        conn_prev.close()

    except:
        start_unit = 0

#  OTHER MONTHS
else:
    prev_month = months[month_index - 1]

    cursor.execute("""
    SELECT end_unit FROM bills 
    WHERE phone=? AND month=? AND year=?
    """, (phone, prev_month, year))

    result = cursor.fetchone()

    if result is None:
        print(f" {prev_month} ka data nahi mila!")
        start_unit = int(input("Enter Start Unit manually: "))
    else:
        start_unit = result[0]

print("Start Unit:", start_unit)

#  END UNIT INPUT
end_unit = int(input(f"Enter End Unit for {month}: "))

if end_unit < start_unit:
    print(" Invalid units")
else:
    units, amount = calculate_bill(start_unit, end_unit)

    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    cursor.execute("""
    INSERT INTO bills 
    (name, phone, month, year, start_unit, end_unit, total_unit, amount, created_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (name, phone, month, year, start_unit, end_unit, units, amount, now))

    conn.commit()

    #   OUTPUT 
    print("\n" + "="*45)
    print("        ELECTRICITY BILL RECEIPT")
    print("="*45)

    print(f"Name        : {name}")
    print(f"Phone       : {phone}")
    print(f"Month       : {month}")

    print("-"*45)
    print(f"{'Start Unit':<20}: {start_unit}")
    print(f"{'End Unit':<20}: {end_unit}")
    print(f"{'Units Used':<20}: {units}")
    print("-"*45)

    print(f"{'Total Amount':<20}: ₹ {amount}")
    print("-"*45)
    print(f"{' Date-Time':<20}: {now}")

    print("="*45)
    print("     PAYMENT SUCCESSFUL ")
    print("="*45)

conn.close()