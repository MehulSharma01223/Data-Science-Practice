import matplotlib.pyplot as plt

# =========================
# DATA
# =========================

x = [1, 2, 3, 4, 5]

sales = [100, 120, 90, 140, 160]

profit = [20, 25, 18, 30, 35]

cities = ["Delhi", "Mumbai", "Pune", "Jaipur"]

city_sales = [500, 650, 400, 300]

marks = [
    45, 50, 52, 55, 60,
    65, 67, 70, 72, 75,
    78, 80, 82, 85, 88
]

# =========================
# FIGURE SIZE
# =========================

plt.figure(figsize=(12,8))

# =========================
# LINE GRAPH
# =========================

plt.subplot(2,2,1)

plt.plot(
    x,
    sales,
    color="blue",
    marker="o"
)

plt.title("Sales Line Plot")

plt.grid(True)

# =========================
# BAR GRAPH
# =========================

plt.subplot(2,2,2)

plt.bar(
    cities,
    city_sales,
    color="orange"
)

plt.title("City Sales Bar Plot")

plt.grid(True)

# =========================
# SCATTER PLOT
# =========================

plt.subplot(2,2,3)

plt.scatter(
    x,
    profit,
    color="green",
    s=100
)

plt.title("Profit Scatter Plot")

plt.grid(True)

# =========================
# HISTOGRAM
# =========================

plt.subplot(2,2,4)

plt.hist(
    marks,
    bins=5,
    color="pink",
    edgecolor="black"
)

plt.title("Marks Histogram")

plt.grid(True)

# =========================
# LAYOUT
# =========================

plt.tight_layout()

# =========================
# SAVE GRAPH
# =========================

plt.savefig("mixed_subplots.png")

# =========================
# SHOW GRAPH
# =========================

plt.show()