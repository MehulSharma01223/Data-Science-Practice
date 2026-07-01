import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# Professional Multi-grid Displot
sns.displot(
    data=tips,
    x="total_bill",
    hue="sex",         # Colors by gender
    col="time",        # Alag columns banayega (Lunch aur Dinner ke)
    kind="kde",        # KDE curve use karega bajaye histogram ke
    fill=True,         # Curves ke andar color fill karega
    palette="Set2",
    height=5,          # Figure ki height
    aspect=1.2         # Width ko thoda stretch karega
)

plt.subplots_adjust(top=0.85) # Title ke liye space
plt.suptitle("Total Bill Distribution by Time and Gender", fontsize=16)

plt.show()
