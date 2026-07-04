import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

titanic = sns.load_dataset("titanic")

plt.figure(figsize=(9,6))

sns.countplot(
    data=titanic,
    x="class",
    hue="survived",
    palette="viridis"
)

plt.title("Passenger Survival by Class", fontsize=15)
plt.xlabel("Passenger Class")
plt.ylabel("Count")

plt.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.show()
