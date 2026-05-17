import matplotlib.pyplot as plt

# =========================
# DATA
# =========================

products = ["Laptop", "Phone", "Tablet", "Watch"]

sales = [70000, 35000, 25000, 15000]

# =========================
# FIGURE SIZE
# =========================

plt.figure(figsize=(8,5))

# =========================
# BAR GRAPH
# =========================

bars = plt.bar(
    products,
    sales,
    color="skyblue"
)

# =========================
# ADD VALUE LABELS
# =========================

for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        str(height),
        ha="center",
        va="bottom"
    )

# =========================
# TITLE & LABELS
# =========================

plt.title("Product Sales with Labels")

plt.xlabel("Products")

plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("bar_labels.png")

plt.show()