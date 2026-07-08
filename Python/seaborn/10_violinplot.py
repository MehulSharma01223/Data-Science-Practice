import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset("titanic")

sns.violinplot(
    data=titanic,
    x="class",
    y="fare",
    hue="sex",
    palette="Set2"
)

plt.show()