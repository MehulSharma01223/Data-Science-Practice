import matplotlib.pyplot as plt

# =========================
# DATA
# =========================

days = [1, 2, 3, 4, 5]

sales = [100, 140, 120, 170, 200]

# =========================
# FIGURE SIZE
# =========================

plt.figure(figsize=(8,5))

# =========================
# LINE PLOT
# =========================

plt.plot(
    days,
    sales,
    color="blue",
    linewidth=3,
    marker="o",
    label="Sales"
)

# =========================
# FILL AREA
# =========================

plt.fill_between(
    days,
    sales,
    color="skyblue",
    alpha=0.4
)

# =========================
# TITLE & LABELS
# =========================

plt.title("Area Plot Example")

plt.xlabel("Days")

plt.ylabel("Sales")

# =========================
# LEGEND
# =========================

plt.legend()

# =========================
# GRID
# =========================

plt.grid(True)

# =========================
# SAVE
# =========================

plt.savefig("area_plot.png")

# =========================
# SHOW
# =========================

plt.show()