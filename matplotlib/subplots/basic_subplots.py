import matplotlib.pyplot as plt

# =========================
# DATA
# =========================

x = [1, 2, 3, 4, 5]

sales = [100, 120, 90, 140, 160]

profit = [20, 25, 18, 30, 35]

# =========================
# FIGURE
# =========================

plt.figure(figsize=(10,5))

# =========================
# SUBPLOT 1
# =========================

plt.subplot(1, 2, 1)

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

plt.subplot(1, 2, 2)

plt.plot(
    x,
    profit,
    color="green",
    marker="s"
)
plt.legend()
plt.title("Profit")

plt.grid(True)

# =========================
# LAYOUT FIX
# =========================

plt.tight_layout()

# =========================
# SAVE GRAPH
# =========================


plt.savefig("basic_subplots.png")

# =========================
# SHOW
# =========================

plt.show()