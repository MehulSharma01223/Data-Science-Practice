import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")
sns.histplot(
    data =iris,
    x = "sepal_length",
    bins=15,
    hue="species",
    
)

sns.rugplot(
    data=iris,
    x="sepal_length",
    hue = "species",
    color ="black"
)

plt.show()
