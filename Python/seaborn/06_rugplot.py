import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")
sns.histplot(
    data =iris,
    x = "sepal_length",
    bins=15
)

sns.rugplot(
    data=iris,
    x="sepal_length",
    color ="black"
)

plt.show()
