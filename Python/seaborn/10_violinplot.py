import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset("titanic")

sns.violinplot(
    data=titanic,
    y="age"
)

plt.show()