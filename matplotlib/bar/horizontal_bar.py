import matplotlib.pyplot as plt

# =========================
# DATA
# =========================

cities = [
    "Delhi",
    "Mumbai",
    "Pune",
    "Jaipur",
    "Chennai"
]

sales = [500, 650, 400, 300, 450]

# =========================
# FIGURE SIZE
# =========================

plt.figure(figsize=(8,5))

# =========================
# HORIZONTAL BAR GRAPH
# =========================

plt.barh(
    cities,
    sales,
    color="orange"
)

# =========================
# TITLE & LABELS
# =========================

plt.title("City-wise Sales")

plt.xlabel("Sales")

plt.ylabel("Cities")

# =========================
# GRID
# =========================

plt.grid(True)

# =========================
# SAVE GRAPH
# =========================

plt.savefig("city_sales_horizontal.png")

# =========================
# SHOW GRAPH
# =========================

plt.show()