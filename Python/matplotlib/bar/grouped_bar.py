import matplotlib.pyplot as plt
import numpy as np

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

profit = [120, 180, 90, 70]

# =========================
# BAR POSITIONS
# =========================

x = np.arange(len(cities))

width = 0.35

# =========================
# FIGURE SIZE
# =========================

plt.figure(figsize=(9,5))

# =========================
# SALES BAR
# =========================

plt.bar(
    x - width/2,
    sales,
    width,
    label="Sales",
    color="blue"
)

# =========================
# PROFIT BAR
# =========================

plt.bar(
    x + width/2,
    profit,
    width,
    label="Profit",
    color="green"
)

# =========================
# X TICKS
# =========================

plt.xticks(
    x,
    cities
)

# =========================
# TITLE & LABELS
# =========================

plt.title("Sales vs Profit")

plt.xlabel("Cities")

plt.ylabel("Amount")

# =========================
# LEGEND
# =========================

plt.legend()

# =========================
# GRID
# =========================

plt.grid(True)

# =========================
# SAVE GRAPH
# =========================

plt.savefig("grouped_bar_graph.png")

# =========================
# SHOW GRAPH
# =========================

plt.show()