import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset("titanic")

sns.boxplot(
    data=titanic,
    y="age"
)

plt.show()

