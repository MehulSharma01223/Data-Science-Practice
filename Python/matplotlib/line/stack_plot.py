import matplotlib.pyplot as plt

# =========================
# DATA
# =========================

days = [1, 2, 3, 4, 5]

mobile_sales = [20, 25, 30, 35, 40]

laptop_sales = [15, 18, 20, 22, 25]

tablet_sales = [10, 12, 15, 18, 20]

# =========================
# FIGURE SIZE
# =========================

plt.figure(figsize=(9,5))

# =========================
# STACK PLOT
# =========================

plt.stackplot(
    days,
    mobile_sales,
    laptop_sales,
    tablet_sales,
    labels=[
        "Mobile",
        "Laptop",
        "Tablet"
    ],
    alpha=0.8
)

# =========================
# TITLE & LABELS
# =========================

plt.title("Product Sales Stack Plot")

plt.xlabel("Days")

plt.ylabel("Sales")

# =========================
# LEGEND
# =========================

plt.legend(loc="upper left")

# =========================
# GRID
# =========================

plt.grid(True)

# =========================
# SAVE
# =========================

# plt.savefig("stack_plot.png")

# =========================
# SHOW
# =========================

plt.show()