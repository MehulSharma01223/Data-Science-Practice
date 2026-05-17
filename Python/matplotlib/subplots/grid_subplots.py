import matplotlib.pyplot as plt

# =========================
# DATA
# =========================

x = [1, 2, 3, 4, 5]

sales = [100, 120, 90, 140, 160]

profit = [20, 25, 18, 30, 35]

customers = [50, 60, 55, 70, 80]

orders = [10, 12, 8, 15, 18]

# =========================
# FIGURE SIZE
# =========================

plt.figure(figsize=(12,8))

# =========================
# SUBPLOT 1
# =========================

plt.subplot(2,2,1)

plt.plot(
    x,
    sales,
    color="blue",
    marker="o"
)

plt.title("Sales")

plt.grid(True)

# =========================
# SUBPLOT 2
# =========================

plt.subplot(2,2,2)

plt.plot(
    x,
    profit,
    color="green",
    marker="s"
)

plt.title("Profit")

plt.grid(True)

# =========================
# SUBPLOT 3
# =========================

plt.subplot(2,2,3)

plt.plot(
    x,
    customers,
    color="orange",
    marker="^"
)

plt.title("Customers")

plt.grid(True)

# =========================
# SUBPLOT 4
# =========================

plt.subplot(2,2,4)

plt.plot(
    x,
    orders,
    color="red",
    marker="*"
)

plt.title("Orders")

plt.grid(True)

# =========================
# LAYOUT
# =========================

plt.tight_layout()

# =========================
# SAVE GRAPH
# =========================

plt.savefig("grid_subplots.png")

# =========================
# SHOW GRAPH
# =========================

plt.show()