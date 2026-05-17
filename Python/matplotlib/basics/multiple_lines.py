import matplotlib.pyplot as plt

# =========================
# DATA
# =========================

days = [1, 2, 3, 4, 5]

sales = [100, 120, 90, 140, 160]

profit = [20, 25, 18, 30, 35]

# =========================
# FIGURE SIZE
# =========================

plt.figure(figsize=(9,5))

# =========================
# SALES LINE
# =========================

plt.plot(
    days,
    sales,
    color="blue",
    marker="o",
    linewidth=3,
    label="Sales"
)

# =========================
# PROFIT LINE
# =========================

plt.plot(
    days,
    profit,
    color="green",
    marker="s",
    linewidth=3,
    linestyle="--",
    label="Profit"
)

# =========================
# TITLE & LABELS
# =========================

plt.title("Sales vs Profit")

plt.xlabel("Days")

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

plt.savefig("sales_profit_graph.png")

# =========================
# SHOW GRAPH
# =========================

plt.show()