import pandas as pd
import matplotlib.pyplot as plt

# Data load
df = pd.DataFrame({
    "Name": ["A","B","C","D","E","F","G","H"],
    "City": ["Delhi","Mumbai","Delhi","Pune","Chennai","Delhi","Mumbai","Pune"],
    "Marks": [80, 55, 90, 40, 70, 85, 60, 30]
})

# City-wise average marks
avg = df.groupby("City")["Marks"].mean()

# Bar chart
avg.plot(kind='bar')

plt.title("City-wise Average Marks")
plt.xlabel("City")
plt.ylabel("Average Marks")

plt.show()


student_count = df["City"].value_counts()

student_count.plot(kind="bar")

plt.title("Number of Students per City")
plt.xlabel("City")
plt.ylabel("Number of Students")

plt.show()

#  Questions of bar chart 

# 1. )   City-wise students count ka graph banaoge
df.groupby("City").size().plot(kind= "bar", color = "pink")
plt.title("Number of Students per City")
plt.xlabel("City")
plt.ylabel("Number of students")

plt.show()

# Q2 ): City-wise average marks ka graph banaoge
df.groupby("City")["Marks"].mean().plot(kind = "bar" , color = "violet")
plt.title("City wise average marks")
plt.ylabel("Average number")
plt.xlabel("City")
plt.show()


#  Q3 .)  top 3 students 
top = df.sort_values("Marks" , ascending = False).head(3)

top.plot(
    x="Name",
    y="Marks",
    kind="bar",
    color="skyblue"
)
plt.title("Top 3 Students")
plt.ylabel("Marks")
plt.xlabel("Students Name")
plt.show()
