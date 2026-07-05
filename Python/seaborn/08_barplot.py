import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset("titanic")

sns.barplot(
    data=titanic,
    x="class",
    y="fare"
)

plt.show()