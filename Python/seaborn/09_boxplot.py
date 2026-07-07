import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

titanic = sns.load_dataset("titanic")

plt.figure(figsize=(10,6))

sns.boxplot(
    data=titanic,
    x="class",
    y="fare",
    hue="sex",
    palette="Set2",
    linewidth=1.5
)

plt.title("Fare Distribution by Passenger Class and Gender")
plt.xlabel("Passenger Class")
plt.ylabel("Fare")

plt.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.show()