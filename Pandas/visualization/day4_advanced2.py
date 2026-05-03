import pandas as pd
import matplotlib.pyplot as plt

# # Data load
df = pd.DataFrame({
    "Name": ["A","B","C","D","E","F","G","H","I","J"],
    "City": ["Delhi","Mumbai","Delhi","Pune","Chennai","Delhi","Mumbai","Pune","Chennai","Delhi"],
    "Marks": [80, 55, 90, 40, 70, 85, 60, 30, 75, 65],
    "Age": [21,22,23,20,22,24,23,21,22,20]
})


#  Q1.)  Har city me 60 se upar marks wale students ka percentage graph banao.

# Requirement:
# 1. City-wise total students count
# 2. City-wise Marks > 60 students count
# 3. Percentage calculate karo
# 4. Bar chart banao

# X-axis: City
# Y-axis: Percentage

# 1. City-wise total students count
a = df.groupby("City").size()
print(a)


# 2. City-wise Marks > 60 students count
h=df[df["Marks"] > 60].groupby("City").size()
print(h)

# 3. Percentage calculate karo
high_students = df[df["Marks"] > 60].groupby("City").size() 
total_students = df.groupby("City").size()
percentage = (high_students / total_students).fillna(0) * 100
print(percentage)

percentage.plot(
    kind = "bar",
    color = "yellow",
    xlabel = "City",
    ylabel = "percentage(%)"

)
plt.show()

