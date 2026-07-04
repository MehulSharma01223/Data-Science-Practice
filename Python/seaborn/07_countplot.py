import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset("titanic")

sns.countplot(
    data=titanic,
    x="sex",
    hue = "survived",
    palette= "Set2"
)

plt.show()