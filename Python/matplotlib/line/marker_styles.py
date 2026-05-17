import matplotlib.pyplot as plt

# =========================
# DATA
# =========================

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

# =========================
# FIGURE SIZE
# =========================

plt.figure(figsize=(10,6))

# =========================
# MARKER 1
# =========================

plt.plot(
    x,
    y,
    marker="o",
    linewidth=2,
    label="Circle"
)

# =========================
# MARKER 2
# =========================

plt.plot(
    x,
    [i + 5 for i in y],
    marker="s",
    linewidth=2,
    label="Square"
)

# =========================
# MARKER 3
# =========================

plt.plot(
    x,
    [i + 10 for i in y],
    marker="^",
    linewidth=2,
    label="Triangle"
)

# =========================
# MARKER 4
# =========================

plt.plot(
    x,
    [i + 15 for i in y],
    marker="*",
    linewidth=2,
    label="Star"
)

# =========================
# MARKER 5
# =========================

plt.plot(
    x,
    [i + 20 for i in y],
    marker="D",
    linewidth=2,
    label="Diamond"
)

# =========================
# TITLE & LABELS
# =========================

plt.title("Marker Styles Comparison")

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

plt.savefig("marker_styles.png")

# =========================
# SHOW
# =========================

plt.show()