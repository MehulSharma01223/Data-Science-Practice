import matplotlib.pyplot as plt

# =========================
# DATA
# =========================

study_hours = [1, 2, 3, 4, 5, 6, 7, 8]

marks = [45, 50, 58, 65, 72, 80, 88, 95]

colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple",
    "pink",
    "black"
]

sizes = [50, 80, 100, 120, 140, 160, 180, 200]

# =========================
# FIGURE SIZE
# =========================

plt.figure(figsize=(8,5))

# =========================
# SCATTER PLOT
# =========================

plt.scatter(
    study_hours,
    marks,
    color=colors,
    s=sizes
)

# =========================
# TITLE & LABELS
# =========================

plt.title("Colored Scatter Plot")

plt.xlabel("Study Hours")

plt.ylabel("Marks")

# =========================
# GRID
# =========================

plt.grid(True)

# =========================
# SAVE GRAPH
# =========================

plt.savefig("colored_scatter.png")

# =========================
# SHOW GRAPH
# =========================

plt.show()