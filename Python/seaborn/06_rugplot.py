import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")
sns.kdeplot(
    data =iris,
    x = "sepal_length",
    fill=True
)

sns.rugplot(
    data=iris,
    x="sepal_length",
    color ="black"
)

plt.show()
