import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

sns.set_theme(style="whitegrid")

titanic = sns.load_dataset("titanic")

plt.figure(figsize=(10,6))

sns.barplot(
    data=titanic,
    x="class",
    y="fare",
    hue="sex",
    estimator=np.mean,
    errorbar=None,
    palette="viridis"
)

plt.title("Average Fare by Passenger Class and Gender", fontsize=15)
plt.xlabel("Passenger Class")
plt.ylabel("Average Fare")

plt.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.show()
