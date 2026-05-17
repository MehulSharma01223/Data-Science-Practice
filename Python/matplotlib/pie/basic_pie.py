import matplotlib.pyplot as plt

# =========================
# DATA
# =========================

cities = [
    "Delhi",
    "Mumbai",
    "Pune",
    "Jaipur"
]

sales = [500, 650, 400, 300]

# =========================
# FIGURE SIZE
# =========================

plt.figure(figsize=(7,7))

# =========================
# PIE CHART
# =========================

plt.pie(
    sales,
    labels=cities,
    autopct="%1.1f%%"
)

# =========================
# TITLE
# =========================

plt.title("City-wise Sales Contribution")

# =========================
# SAVE GRAPH
# =========================

# plt.savefig("basic_pie_chart.png")

# =========================
# SHOW GRAPH
# =========================

plt.show()