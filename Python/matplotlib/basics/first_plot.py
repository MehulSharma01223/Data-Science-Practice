import matplotlib.pyplot as plt

# =========================
# DATA
# =========================

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]

# =========================
# LINE PLOT
# =========================

plt.plot(x, y)

# =========================
# TITLES & LABELS
# =========================

plt.title("First Line Graph")

plt.xlabel("X Values")

plt.ylabel("Y Values")

# =========================
# SHOW GRAPH
# =========================

plt.show()