import matplotlib.pyplot as plt

# =========================
# DATA
# =========================

months = ["Jan", "Feb", "Mar", "Apr", "May"]

sales = [100, 140, 120, 170, 200]

# =========================
# FIGURE & AXIS
# =========================

fig, ax = plt.subplots(figsize=(8,5))

# =========================
# BACKGROUND COLORS
# =========================

fig.patch.set_facecolor("lightgray")

ax.set_facecolor("whitesmoke")

# =========================
# LINE GRAPH
# =========================

ax.plot(
    months,
    sales,
    color="blue",
    marker="o",
    linewidth=3
)

# =========================
# TITLE & LABELS
# =========================

ax.set_title(
    "Customized Background Graph",
    fontsize=16,
    fontweight="bold"
)

ax.set_xlabel("Months")

ax.set_ylabel("Sales")

# =========================
# GRID
# =========================

ax.grid(True)

# =========================
# SAVE
# =========================

plt.savefig("background_axis.png")

# =========================
# SHOW
# =========================

plt.show()