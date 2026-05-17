import matplotlib.pyplot as plt

# =========================
# DATA
# =========================

months = ["Jan", "Feb", "Mar", "Apr", "May"]

sales = [100, 140, 120, 170, 200]

styles = [
    "ggplot",
    "dark_background",
    "classic",
    "Solarize_Light2"
]

# =========================
# LOOP THROUGH STYLES
# =========================

for style in styles:

    plt.style.use(style)

    plt.figure(figsize=(8,5))

    plt.plot(
        months,
        sales,
        marker="o",
        linewidth=3
    )

    plt.title(f"Style: {style}")

    plt.xlabel("Months")

    plt.ylabel("Sales")

    plt.grid(True)

    plt.savefig(f"{style}.png")

    plt.show()