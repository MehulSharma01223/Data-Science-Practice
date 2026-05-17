import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

# =========================
# DATA
# =========================

x = [1, 2, 3, 4, 5]

y = [10, 20, 25, 30, 40]

z = [5, 10, 15, 20, 25]

# =========================
# FIGURE
# =========================

fig = plt.figure(figsize=(8,6))

# =========================
# 3D AXIS
# =========================

ax = fig.add_subplot(
    111,
    projection="3d"
)

# =========================
# 3D SCATTER
# =========================

ax.scatter(
    x,
    y,
    z,
    color="red",
    s=100
)

# =========================
# LABELS
# =========================

ax.set_title("Basic 3D Scatter Plot")

ax.set_xlabel("X Axis")

ax.set_ylabel("Y Axis")

ax.set_zlabel("Z Axis")

# =========================
# SAVE
# =========================

plt.savefig("basic_3d_plot.png")

# =========================
# SHOW
# =========================

plt.show()