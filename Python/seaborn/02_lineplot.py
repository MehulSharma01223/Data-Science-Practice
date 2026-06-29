import seaborn as sns
import matplotlib.pyplot as plt

flights = sns.load_dataset("flights")

plt.figure(figsize=(10,6))

sns.lineplot(
    data=flights,
    x="year",
    y="passengers",
    hue="month",
    palette="tab20",
    linewidth=2,
    marker="o",
    errorbar=None
)

plt.title("Passenger Growth Over Years")

plt.xlabel("Year")

plt.ylabel("Passengers")

plt.grid(alpha=0.3)

plt.tight_layout()

plt.show()

