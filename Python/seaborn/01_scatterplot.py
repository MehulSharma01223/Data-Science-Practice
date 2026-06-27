import seaborn as sns
import matplotlib.pyplot as plt

# ==========================
# Load Dataset
# ==========================

tips = sns.load_dataset("tips")

# ==========================
# Create Figure
# ==========================

plt.figure(figsize=(10, 6))

# ==========================
# Scatter Plot
# ==========================

sns.scatterplot(
    data=tips,                 # Dataset
    x="total_bill",            # X-axis
    y="tip",                   # Y-axis
    hue="day",                 # Color based on day
    style="time",              # Marker shape
    size="size",               # Marker size
    palette="Set2",            # Color palette

    hue_order=["Thur", "Fri", "Sat", "Sun"],
    markers="+",
    legend="brief",

    alpha=0.8,
    edgecolor="black",
    linewidth=0.5
)

# ==========================
# Customization
# ==========================

plt.title("Total Bill vs Tip", fontsize=16)
plt.xlabel("Total Bill ($)", fontsize=12)
plt.ylabel("Tip ($)", fontsize=12)

plt.grid(alpha=0.3)

plt.tight_layout()

plt.show()