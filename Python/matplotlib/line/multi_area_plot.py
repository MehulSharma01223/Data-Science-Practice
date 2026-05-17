import matplotlib.pyplot as plt

# =========================
# DATA
# =========================

days = [1, 2, 3, 4, 5]

sales = [100, 140, 120, 170, 200]

profit = [20, 30, 25, 40, 50]

# =========================
# FIGURE SIZE
# =========================

plt.figure(figsize=(9,5))

# =========================
# SALES LINE
# =========================

plt.plot(
    days,
    sales,
    color="blue",
    linewidth=3,
    label="Sales"
)

# =========================
# SALES AREA
# =========================

plt.fill_between(
    days,
    sales,
    color="skyblue",
    alpha=0.4
)

# =========================
# PROFIT LINE
# =========================

plt.plot(
    days,
    profit,
    color="green",
    linewidth=3,
    label="Profit"
)

# =========================
# PROFIT AREA
# =========================

plt.fill_between(
    days,
    profit,
    color="lightgreen",
    alpha=0.5
)

# =========================
# TITLE & LABELS
# =========================

plt.title("Sales vs Profit Area Plot")

plt.xlabel("Days")

plt.ylabel("Amount")

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

plt.savefig("multi_area_plot.png")

# =========================
# SHOW
# =========================

plt.show()