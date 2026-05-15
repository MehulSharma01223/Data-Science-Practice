import matplotlib.pyplot as plt
import numpy as np

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
# MEAN
# =========================

mean_marks = np.mean(marks)

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
# MEAN LINE
# =========================

plt.axvline(
    mean_marks,
    color="red",
    linewidth=3,
    linestyle="--",
    label=f"Mean = {mean_marks:.2f}"
)

# =========================
# TITLE & LABELS
# =========================

plt.title("Histogram with Mean Line")

plt.xlabel("Marks Range")

plt.ylabel("Frequency")

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

plt.savefig("histogram_mean.png")

# =========================
# SHOW GRAPH
# =========================

plt.show()