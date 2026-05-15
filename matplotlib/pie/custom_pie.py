import matplotlib.pyplot as plt

# =========================
# DATA
# =========================

products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Accessories"
]

sales = [500, 350, 200, 150]

colors = [
    "skyblue",
    "orange",
    "green",
    "pink"
]

explode = [0.1, 0, 0, 0]

# =========================
# FIGURE SIZE
# =========================

plt.figure(figsize=(7,7))

# =========================
# PIE CHART
# =========================

plt.pie(
    sales,
    labels=products,
    colors=colors,
    autopct="%1.1f%%",
    explode=explode,
    shadow=True
)

# =========================
# TITLE
# =========================

plt.title("Product Sales Contribution")

# =========================
# SAVE GRAPH
# =========================

plt.savefig("custom_pie_chart.png")

# =========================
# SHOW GRAPH
# =========================

plt.show()