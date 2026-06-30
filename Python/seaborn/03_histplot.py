import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

tips = sns.load_dataset("tips")

plt.figure(figsize=(10,6))

sns.histplot(
    data=tips,
    x="total_bill",
    bins=20,
    kde=True,
    hue="sex",
    palette="Set2",
    alpha=0.6,
    stat="count",
    multiple ="dodge"
)

plt.title("Distribution of Total Bill")

plt.xlabel("Total Bill ($)")

plt.ylabel("Count")

plt.grid(alpha=0.3)

plt.tight_layout()

plt.show()

