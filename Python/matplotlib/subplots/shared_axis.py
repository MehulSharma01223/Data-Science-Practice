import matplotlib.pyplot as plt

# =========================
# DATA
# =========================

days = [1, 2, 3, 4, 5]

sales = [100, 120, 90, 140, 160]

profit = [20, 25, 18, 30, 35]

orders = [10, 12, 8, 15, 18]

# =========================
# CREATE SUBPLOTS
# =========================

fig, axes = plt.subplots(
    3,
    1,
    figsize=(8,10),
    sharex=True
)

# =========================
# SALES
# =========================

axes[0].plot(
    days,
    sales,
    color="blue",
    marker="o"
)

axes[0].set_title("Sales")

axes[0].grid(True)

# =========================
# PROFIT
# =========================

axes[1].plot(
    days,
    profit,
    color="green",
    marker="s"
)

axes[1].set_title("Profit")

axes[1].grid(True)

# =========================
# ORDERS
# =========================

axes[2].plot(
    days,
    orders,
    color="red",
    marker="^"
)

axes[2].set_title("Orders")

axes[2].grid(True)

# =========================
# COMMON X LABEL
# =========================

plt.xlabel("Days")

# =========================
# LAYOUT
# =========================

plt.tight_layout()

# =========================
# SAVE
# =========================

plt.savefig("shared_axis_subplots.png")

# =========================
# SHOW
# =========================

plt.show()