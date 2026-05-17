import matplotlib.pyplot as plt

# =========================
# DATA
# =========================

study_hours = [1, 2, 3, 4, 5, 6, 7, 8]

marks = [45, 50, 58, 65, 72, 80, 88, 95]

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
    color="red",
    s=100
)

# =========================
# TITLE & LABELS
# =========================

plt.title("Study Hours vs Marks")

plt.xlabel("Study Hours")

plt.ylabel("Marks")

# =========================
# GRID
# =========================

plt.grid(True)

# =========================
# SAVE GRAPH
# =========================

plt.savefig("study_hours_scatter.png")

# =========================
# SHOW GRAPH
# =========================

plt.show()