import matplotlib.pyplot as plt

# =========================
# DATA
# =========================

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

# =========================
# FIGURE SIZE
# =========================

plt.figure(figsize=(8, 5))

# =========================
# CUSTOM LINE PLOT
# =========================

plt.plot(
    x,
    y,
    color="red",
    marker="^",
    linestyle=":",
    linewidth=3
)

# =========================
# TITLES & LABELS
# =========================

plt.title("Customized Line Graph")

plt.xlabel("X Values")

plt.ylabel("Y Values")

# =========================
# GRID
# =========================

plt.grid(True)

# =========================
# SHOW GRAPH
# =========================

plt.show()