import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="dark")

df = sns.load_dataset("iris")

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

sns.kdeplot(
    data=df,
    x="sepal_length",
    fill=True,
    color="crimson",
    bw_adjust=1.0,
    ax=axes[0],
)

axes[0].set_title("Univariate KDE: Sepal Length Distribution", fontsize=12)
axes[0].set_xlabel("Sepal Length (cm)")
axes[0].set_ylabel("Density")

sns.kdeplot(
    data=df,
    x="sepal_length",
    hue="species",
    fill=True,
    palette="muted",
    alpha=0.4,
    linewidth=2,
    ax=axes[1],
)

axes[1].set_title("Professional Multi-Class KDE: Sepal Length by Species", fontsize=12)
axes[1].set_xlabel("Sepal Length (cm)")
axes[1].set_ylabel("Density")

plt.tight_layout()
plt.show()
