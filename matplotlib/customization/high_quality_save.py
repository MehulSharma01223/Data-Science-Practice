import matplotlib.pyplot as plt

# =========================
# DATA
# =========================

months = ["Jan", "Feb", "Mar", "Apr", "May"]

sales = [100, 140, 120, 170, 200]

# =========================
# FIGURE SIZE
# =========================

plt.figure(figsize=(8,5))

# =========================
# LINE GRAPH
# =========================

plt.plot(
    months,
    sales,
    marker="o",
    linewidth=3,
    color="blue"
)

# =========================
# TITLE & LABELS
# =========================

plt.title("High Quality Saved Graph")

plt.xlabel("Months")

plt.ylabel("Sales")

plt.grid(True)

# =========================
# HIGH QUALITY SAVE
# =========================

plt.savefig(
    "high_quality_graph.png",
    dpi=300,
    bbox_inches="tight"
)

# =========================
# SHOW
# =========================

plt.show()