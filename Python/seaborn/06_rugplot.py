import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

iris = sns.load_dataset("iris")

plt.figure(figsize=(10,6))

sns.kdeplot(
    data=iris,
    x="sepal_length",
    fill=True,
    color="skyblue"
)

sns.rugplot(
    data=iris,
    x="sepal_length",
    hue="species",
    height=0.06,
    palette="Dark2",
    alpha=0.8
)

plt.title("Sepal Length Distribution with Rug Plot")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Density")

plt.tight_layout()
plt.show()
