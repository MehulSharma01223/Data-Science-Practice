import matplotlib.pyplot as plt

# =========================
# DATA
# =========================

x = [1, 2, 3, 4, 5]

y1 = [10, 20, 15, 30, 25]

y2 = [15, 25, 20, 35, 30]

y3 = [5, 15, 10, 20, 18]

y4 = [12, 18, 14, 28, 22]

# =========================
# FIGURE SIZE
# =========================

plt.figure(figsize=(9,5))

# =========================
# LINE 1
# =========================

plt.plot(
    x,
    y1,
    linestyle="-",
    linewidth=3,
    label="Solid"
)

# =========================
# LINE 2
# =========================

plt.plot(
    x,
    y2,
    linestyle="--",
    linewidth=3,
    label="Dashed"
)

# =========================
# LINE 3
# =========================

plt.plot(
    x,
    y3,
    linestyle=":",
    linewidth=3,
    label="Dotted"
)

# =========================
# LINE 4
# =========================

plt.plot(
    x,
    y4,
    linestyle="-.",
    linewidth=3,
    label="Dash Dot"
)

# =========================
# TITLE & LABELS
# =========================

plt.title("Line Styles Comparison")

plt.xlabel("X Values")

plt.ylabel("Y Values")

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

plt.savefig("line_styles.png")

# =========================
# SHOW
# =========================

plt.show()