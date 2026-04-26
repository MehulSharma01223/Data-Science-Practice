import pandas as pd
import matplotlib.pyplot as plt

# # Data load
df = pd.DataFrame({
    "Name": ["A","B","C","D","E","F","G","H","I","J"],
    "City": ["Delhi","Mumbai","Delhi","Pune","Chennai","Delhi","Mumbai","Pune","Chennai","Delhi"],
    "Marks": [80, 55, 90, 40, 70, 85, 60, 30, 75, 65],
    "Age": [21,22,23,20,22,24,23,21,22,20]
})

# # City-wise average marks
# avg = df.groupby("City")["Marks"].mean()

# # Bar chart
# avg.plot(kind='bar')

# plt.title("City-wise Average Marks")
# plt.xlabel("City")
# plt.ylabel("Average Marks")

# plt.show()


# student_count = df["City"].value_counts()

# student_count.plot(kind="bar")

# plt.title("Number of Students per City")
# plt.xlabel("City")
# plt.ylabel("Number of Students")

# plt.show()

# #  Questions of bar chart 

# # 1. )   City-wise students count ka graph banaoge
# df.groupby("City").size().plot(kind= "bar", color = "pink")
# plt.title("Number of Students per City")
# plt.xlabel("City")
# plt.ylabel("Number of students")

# plt.show()

# # Q2 ): City-wise average marks ka graph banaoge
# df.groupby("City")["Marks"].mean().plot(kind = "bar" , color = "violet")
# plt.title("City wise average marks")
# plt.ylabel("Average number")
# plt.xlabel("City")
# plt.show()


# #  Q3 .)  top 3 students 
# top = df.sort_values("Marks" , ascending = False).head(3)

# top.plot(
#     x="Name",
#     y="Marks",
#     kind="bar",
#     color="skyblue"
# )
# plt.title("Top 3 Students")
# plt.ylabel("Marks")
# plt.xlabel("Students Name")
# plt.show()


# #  Q1: Sirf Delhi aur Mumbai ke students ka marks bar chart banao

# df[df["City"].isin(["Delhi","Mumbai"])]\
#     .groupby("City")["Marks"].mean().plot(kind = "bar" , color = "pink")

# plt.title("City wise average marks")
# plt.ylabel("Average Marks")
# plt.xlabel("City")
# plt.show()


# #  Q2.) 60 se upar marks wale students ka city-wise count graph banao

# df[df["Marks"] > 60 ]\
#     .groupby("City").size()\
#     .plot(kind = "bar" , color = "yellow")

# plt.title("students name city wise")
# plt.ylabel(" Student Name")
# plt.xlabel("City")
# plt.show()


# # Q 3. ) Q3: Marks ka histogram banao

# df["Marks"].plot(kind = "hist" , color = "yellow")

# plt.title("Marks Distribution")
# plt.xlabel("Marks")
# plt.ylabel("Frequency")

# plt.show()

# City-wise minimum marks ka bar chart banao
df.groupby("City")["Marks"].min().plot(kind = "bar" , color = "blue")
plt.title("City Wise minimum marks")
plt.xlabel("City")
plt.ylabel("Minimum Marks")
plt.show()

# City-wise maximum marks ka bar chart

df.groupby("City")["Marks"].max().plot(kind = "bar" , color = "pink")
plt.title("City Wise topper students marks")
plt.xlabel("City")
plt.ylabel(" Marks")
plt.show()

# Marks > 50 aur Age < 23 wale students ka graph
z = df[(df["Marks"] > 50 ) & (df["Age"] < 23)]
z.plot(
    x = "Name",
    y = "Marks",
    kind = "bar",
    color = "grey",
)
plt.title("Students (Marks > 50 & Age < 23)")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.show()