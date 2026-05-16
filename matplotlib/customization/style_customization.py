import matplotlib.pyplot as plt

# =========================
# STYLE
# =========================

# plt.style.use("ggplot")


plt.style.use("classic")

# plt.style.use("dark_background")

# plt.style.use("fast")

# plt.style.use("bmh")

# plt.style.use("fivethirtyeight")

# plt.style.use("grayscale")

# plt.style.use("seaborn-v0_8")

# plt.style.use("seaborn-v0_8-dark")

# plt.style.use("seaborn-v0_8-whitegrid")

# plt.style.use("seaborn-v0_8-darkgrid")

# plt.style.use("Solarize_Light2")

# plt.style.use("tableau-colorblind10")

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
    color="blue",
    marker="o",
    linewidth=3
)

# =========================
# TITLE & LABELS
# =========================

plt.title(
    "Monthly Sales Report",
    fontsize=18,
    fontweight="bold"
)

plt.xlabel(
    "Months",
    fontsize=12
)

plt.ylabel(
    "Sales",
    fontsize=12
)

# =========================
# GRID
# =========================

plt.grid(True)

# =========================
# SAVE
# =========================

plt.savefig("style_customization.png")

# =========================
# SHOW
# =========================

plt.show()