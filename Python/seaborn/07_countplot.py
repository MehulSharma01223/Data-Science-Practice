import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset("titanic")

sns.countplot(
    data=titanic,
    x="sex"
)

plt.show()