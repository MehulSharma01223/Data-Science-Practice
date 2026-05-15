import matplotlib.pyplot as plt

# =========================
# DATA
# =========================

marks = [
    45, 50, 52, 55, 60,
    65, 67, 70, 72, 75,
    78, 80, 82, 85, 88,
    90, 92, 95
]

# =========================
# FIGURE SIZE
# =========================

plt.figure(figsize=(8,5))

# =========================
# HISTOGRAM
# =========================

plt.hist(
    marks,
    bins=5,
    color="skyblue",
    edgecolor="black"
)

# =========================
# TITLE & LABELS
# =========================

plt.title("Marks Distribution")

plt.xlabel("Marks Range")

plt.ylabel("Frequency")

# =========================
# GRID
# =========================

plt.grid(True)

# =========================
# SAVE GRAPH
# =========================

plt.savefig("basic_histogram.png")

# =========================
# SHOW GRAPH
# =========================

plt.show()