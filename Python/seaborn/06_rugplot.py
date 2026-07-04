import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

sns.rugplot(
    data=iris,
    x="sepal_length"
)

plt.show()
