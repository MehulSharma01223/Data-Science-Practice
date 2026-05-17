import matplotlib.pyplot as plt

# =========================
# DATA
# =========================

months = ["Jan", "Feb", "Mar", "Apr", "May"]

sales = [100, 140, 120, 170, 200]

profit = [20, 30, 25, 40, 50]

orders = [10, 12, 9, 15, 18]

categories = [
    "Mobile",
    "Laptop",
    "Tablet",
    "Accessories"
]

category_sales = [400, 350, 200, 150]

# =========================
# FIGURE
# =========================

plt.figure(figsize=(14,10))

# =========================
# SUBPLOT 1
# =========================

plt.subplot(2,2,1)

plt.plot(
    months,
    sales,
    marker="o",
    linewidth=3,
    color="blue"
)

plt.title("Monthly Sales")

plt.grid(True)

# =========================
# SUBPLOT 2
# =========================

plt.subplot(2,2,2)

plt.bar(
    months,
    profit,
    color="green"
)

plt.title("Monthly Profit")

plt.grid(True)

# =========================
# SUBPLOT 3
# =========================

plt.subplot(2,2,3)

plt.scatter(
    months,
    orders,
    color="red",
    s=120
)

plt.title("Orders Analysis")

plt.grid(True)

# =========================
# SUBPLOT 4
# =========================

plt.subplot(2,2,4)

plt.pie(
    category_sales,
    labels=categories,
    autopct="%1.1f%%"
)

plt.title("Category Contribution")

# =========================
# LAYOUT
# =========================

plt.tight_layout()

# =========================
# SAVE
# =========================

plt.savefig(
    "sales_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

# =========================
# SHOW
# =========================

plt.show()