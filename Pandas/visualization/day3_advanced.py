import pandas as pd
import matplotlib.pyplot as plt

# # Data load
df = pd.DataFrame({
    "Name": ["A","B","C","D","E","F","G","H","I","J"],
    "City": ["Delhi","Mumbai","Delhi","Pune","Chennai","Delhi","Mumbai","Pune","Chennai","Delhi"],
    "Marks": [80, 55, 90, 40, 70, 85, 60, 30, 75, 65],
    "Age": [21,22,23,20,22,24,23,21,22,20]
})



#  Q13: City-wise average age graph
df.groupby("City")["Age"].mean().plot(kind = "bar" , color = "pink")
plt.title("City-wise Average Age")
plt.xlabel("City")
plt.ylabel("Average Age")
plt.show()

#  Q14:  Marks ko descending sort karke line chart banao
line = df.sort_values(by="Marks", ascending=False)
line.plot(
    x="Name",
    y="Marks",
    kind="line",
    color="yellow"
)

plt.title("Marks Trend (Descending)")
plt.xlabel("Name")
plt.ylabel("Marks")


plt.show()

#  Q 15 : Har city ke topper ka bar chart banao

topper = df.loc[df.groupby("City")["Marks"].idxmax()]

topper.plot(
    x="Name",
    y="Marks",
    kind="bar",
    color="brown"
)

plt.title("City-wise Topper Students")
plt.xlabel("Student Name")
plt.ylabel("Marks")

plt.show()