import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

titanic = sns.load_dataset("titanic")

sns.barplot(
    data=titanic,
    x="class",
    y="fare",
    hue="sex",
    palette="Set2",
    estimator=np.median
)

plt.show()