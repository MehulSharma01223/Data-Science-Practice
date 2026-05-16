import matplotlib.pyplot as plt

# =========================
# DATA
# =========================

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May"
]

sales = [100, 150, 120, 180, 200]

# =========================
# FIGURE SIZE
# =========================

plt.figure(figsize=(8,5))

# =========================
# LINE PLOT
# =========================

plt.plot(
    months,
    sales,
    marker="o",
    linewidth=3,
    color="blue"
)

# =========================
# ANNOTATION
# =========================

plt.annotate(
    "Highest Sales",
    xy=("May", 200),
    xytext=("Mar", 220),
    arrowprops=dict(
        facecolor="black",
        shrink=0.05
    )
)

# =========================
# TITLE & LABELS
# =========================

plt.title("Monthly Sales")

plt.xlabel("Months")

plt.ylabel("Sales")

# =========================
# GRID
# =========================

plt.grid(True)

# =========================
# SAVE
# =========================

plt.savefig("annotations_plot.png")

# =========================
# SHOW
# =========================

plt.show()