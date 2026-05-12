import pandas as pd
import matplotlib.pyplot as plt

# =====================
# ELECTRONICS SALES DATA
# =====================

df = pd.DataFrame({
    "Order_ID": [101,102,103,104,105,106,107,108,109,110,
                 111,112,113,114,115,116,117,118,119,120],

    "City": [
        "Delhi","Mumbai","Pune","Delhi","Bangalore",
        "Mumbai","Pune","Delhi","Chennai","Bangalore",
        "Mumbai","Delhi","Pune","Chennai","Mumbai",
        "Delhi","Bangalore","Pune","Chennai","Delhi"
    ],

    "Product": [
        "Laptop","Phone","Tablet","Headphones","Laptop",
        "Smartwatch","Phone","Tablet","Laptop","Phone",
        "Headphones","Smartwatch","Laptop","Tablet","Phone",
        "Laptop","Headphones","Smartwatch","Phone","Tablet"
    ],

    "Category": [
        "Computers","Mobiles","Mobiles","Accessories","Computers",
        "Wearables","Mobiles","Mobiles","Computers","Mobiles",
        "Accessories","Wearables","Computers","Mobiles","Mobiles",
        "Computers","Accessories","Wearables","Mobiles","Mobiles"
    ],

    "Sales": [
        70000,30000,25000,5000,80000,
        15000,35000,27000,75000,32000,
        6000,18000,82000,26000,34000,
        72000,7000,17000,36000,28000
    ],

    "Quantity": [
        2,3,1,5,2,
        2,4,2,1,3,
        6,2,2,1,4,
        2,5,2,3,2
    ],

    "Payment_Mode": [
        "UPI","Card","Cash","UPI","Card",
        "UPI","Cash","Card","UPI","Cash",
        "Card","UPI","Card","Cash","UPI",
        "Card","Cash","UPI","Card","Cash"
    ]
})

# =====================
# SAVE DATA TO CSV
# =====================

df.to_csv(
    r"C:\Users\MAINAK\Desktop\SQl\Pandas\projects\sales_analysis\data\sales_data.csv",
    index=False
)

print("CSV file created successfully.")

# =====================
# ANALYSIS
# =====================

city_sales = df.groupby("City")["Sales"].sum()
product_sales = df.groupby("Product")["Sales"].sum()
avg_city_sales = df.groupby("City")["Sales"].mean()
product_quantity = df.groupby("Product")["Quantity"].sum()
payment_sales = df.groupby("Payment_Mode")["Sales"].sum()
category_sales = df.groupby("Category")["Sales"].sum()

top_orders = df.sort_values(by="Sales", ascending=False).head(5)

city_product_sales = df.pivot_table(
    values="Sales",
    index="City",
    columns="Product",
    aggfunc="sum"
)

payment_count = df["Payment_Mode"].value_counts()
avg_product_sales = df.groupby("Product")["Sales"].mean()
city_quantity = df.groupby("City")["Quantity"].sum()

print("\nCITY-WISE TOTAL SALES:\n", city_sales)
print("\nPRODUCT-WISE TOTAL SALES:\n", product_sales)
print("\nAVERAGE SALES BY CITY:\n", avg_city_sales)
print("\nPRODUCT-WISE TOTAL QUANTITY:\n", product_quantity)
print("\nPAYMENT MODE SALES:\n", payment_sales)
print("\nCATEGORY-WISE TOTAL SALES:\n", category_sales)
print("\nTOP 5 ORDERS:\n", top_orders)
print("\nCITY vs PRODUCT SALES:\n", city_product_sales)
print("\nPAYMENT MODE COUNT:\n", payment_count)
print("\nPRODUCT-WISE AVERAGE SALES:\n", avg_product_sales)
print("\nCITY-WISE TOTAL QUANTITY:\n", city_quantity)

# =====================
# VISUALIZATION PATH
# =====================

visuals_path = r"C:\Users\MAINAK\Desktop\SQl\Pandas\projects\sales_analysis\visuals"

# =====================
# GRAPH 1: CITY-WISE TOTAL SALES
# =====================

city_sales.plot(kind="bar", figsize=(8, 5))
plt.title("City-wise Total Sales")
plt.xlabel("City")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig(visuals_path + r"\city_sales.png")
plt.show()

# =====================
# GRAPH 2: PRODUCT-WISE TOTAL SALES
# =====================

product_sales.plot(kind="bar", figsize=(8, 5))
plt.title("Product-wise Total Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig(visuals_path + r"\product_sales.png")
plt.show()

# =====================
# GRAPH 3: AVERAGE SALES BY CITY
# =====================

avg_city_sales.plot(kind="line", marker="o", figsize=(8, 5))
plt.title("Average Sales by City")
plt.xlabel("City")
plt.ylabel("Average Sales")
plt.tight_layout()
plt.savefig(visuals_path + r"\avg_city_sales.png")
plt.show()

# =====================
# GRAPH 4: PRODUCT-WISE TOTAL QUANTITY
# =====================

product_quantity.plot(kind="bar", figsize=(8, 5))
plt.title("Product-wise Total Quantity")
plt.xlabel("Product")
plt.ylabel("Quantity")
plt.tight_layout()
plt.savefig(visuals_path + r"\product_quantity.png")
plt.show()

# =====================
# GRAPH 5: PAYMENT MODE SALES
# =====================

payment_sales.plot(kind="pie", autopct="%1.1f%%", figsize=(7, 7))
plt.title("Payment Mode Sales")
plt.ylabel("")
plt.tight_layout()
plt.savefig(visuals_path + r"\payment_sales.png")
plt.show()

# =====================
# GRAPH 6: CATEGORY-WISE TOTAL SALES
# =====================

category_sales.plot(kind="bar", figsize=(8, 5))
plt.title("Category-wise Total Sales")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig(visuals_path + r"\category_sales.png")
plt.show()

# =====================
# GRAPH 7: PRODUCT-WISE AVERAGE SALES
# =====================

avg_product_sales.plot(kind="bar", figsize=(8, 5))
plt.title("Product-wise Average Sales")
plt.xlabel("Product")
plt.ylabel("Average Sales")
plt.tight_layout()
plt.savefig(visuals_path + r"\avg_product_sales.png")
plt.show()

# =====================
# GRAPH 8: CITY-WISE TOTAL QUANTITY
# =====================

city_quantity.plot(kind="bar", figsize=(8, 5))
plt.title("City-wise Total Quantity")
plt.xlabel("City")
plt.ylabel("Quantity")
plt.tight_layout()
plt.savefig(visuals_path + r"\city_quantity.png")
plt.show()

# =====================
# GRAPH 9: QUANTITY VS SALES
# =====================

plt.figure(figsize=(8, 5))
plt.scatter(df["Quantity"], df["Sales"])
plt.title("Quantity vs Sales")
plt.xlabel("Quantity")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig(visuals_path + r"\quantity_vs_sales.png")
plt.show()

# =====================
# GRAPH 10: CITY VS PRODUCT SALES
# =====================

city_product_sales.plot(kind="bar", figsize=(10, 6))
plt.title("City vs Product Sales")
plt.xlabel("City")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig(visuals_path + r"\city_product_sales.png")
plt.show()

print("\nProject completed successfully.")
print("CSV saved in data folder.")
print("All graphs saved in visuals folder.")

