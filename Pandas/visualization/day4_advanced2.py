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


# Q2 : City-wise total marks ka pie chart banao

# Requirement:
# 1. City ke basis par Marks ka sum nikaalo
# 2. Pie chart banao

# Labels → City
# Values → Total Marks

city_total = df.groupby("City")["Marks"].sum()

city_total.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("City-wise Total Marks Distribution")
plt.ylabel("")

plt.show()


# Q18: Marks vs Age scatter plot banao

# Requirement:
# 1. X-axis → Age
# 2. Y-axis → Marks
# 3. Scatter plot banao
# 4. Graph dekh ke insight likho:
#    → Age badhne par marks increase ho rahe hain ya random pattern hai?


plt.scatter(df["Age"], df["Marks"], color="blue")
for i in range(len(df)):
    plt.text(df["Age"][i], df["Marks"][i], df["Name"][i])

plt.title("Marks vs Age")
plt.xlabel("Age")
plt.ylabel("Marks")

plt.show()

# Q19: Top 5 students ka comparison graph banao

# Requirement:
# 1. Marks ko descending sort karo
# 2. Top 5 students select karo
# 3. Graph banao

# Graph:
# X-axis → Name
# Y-axis → Marks

# Insight:
# → kaun highest scorer hai?
# → marks gap kaisa hai (close hai ya difference zyada hai)

top5 = df.sort_values(by = "Marks", ascending= False).head(5)
top5.plot(
    kind="bar",
    x="Name",
    y="Marks",
    color="pink"
)

plt.title("Top 5 Students Comparison")
plt.xlabel("Student Name")
plt.ylabel("Marks")

plt.show()


# Q20: City-wise performance category (Good / Average / Poor) ka graph banao

# Requirement:
# 1. City-wise average marks nikaalo
# 2. Average marks ke basis par category banao:
#    - mean > 75 → Good
#    - mean > 60 → Average
#    - else → Poor
# 3. Category ka count graph banao

# Graph:
# X-axis → Performance Category
# Y-axis → Number of Cities

city_avg = df.groupby("City")["Marks"].mean()

def category(x):
    if x > 75:
        return "Good"
    elif x > 60:
        return "Average"
    else:
        return "Poor"

performance_category = city_avg.apply(category)

print(performance_category)

performance_category.value_counts().plot(
    kind="bar",
    color="green"
)

plt.title("City-wise Performance Category")
plt.xlabel("Performance Category")
plt.ylabel("Number of Cities")

plt.show()


# Q21: Marks distribution ko histogram + mean line ke saath show karo

# Requirement:
# 1. Marks ka histogram banao
# 2. Average (mean) calculate karo
# 3. Graph me ek vertical line add karo (mean dikhane ke liye)

# Graph:
# X-axis → Marks
# Y-axis → Frequency

df["Marks"].plot(kind="hist", color="yellow")

mean = df["Marks"].mean()

plt.axvline(mean, color="red", linewidth=2)

plt.title("Marks Distribution with Mean Line")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()

#   Q22: City-wise student count vs average marks ka comparison graph banao

# Goal:
# Check karo → kya jahan students zyada hain wahan performance better hai?
count = df.groupby("City").size()

# Step 2: Average
avg = df.groupby("City")["Marks"].mean()

# Step 3: Combine
combined = pd.DataFrame({
    "Count": count,
    "Average": avg
})

print(combined)

# Step 4: Plot (Dual Axis)
fig, ax1 = plt.subplots()

ax2 = ax1.twinx()

combined["Count"].plot(kind="bar", color="skyblue", ax=ax1, position=0)
combined["Average"].plot(kind="bar", color="orange", ax=ax2, position=1)

# Labels
ax1.set_ylabel("Student Count")
ax2.set_ylabel("Average Marks")

plt.title("City-wise Student Count vs Average Marks")
plt.xlabel("City")

plt.show()

# Q23: Young vs Old students ka marks comparison graph banao

# Goal:
# Check karo → young students better perform karte hain ya old?

# Step 1: Group create
df["Group"] = df["Age"].apply(lambda x: "Young" if x < 23 else "Old")

# Step 2: Average marks
group_avg = df.groupby("Group")["Marks"].mean()

print(group_avg)

# Step 3: Graph
group_avg.plot(
    kind="bar",
    color=["green", "orange"]
)

plt.title("Young vs Old Students Performance")
plt.xlabel("Group")
plt.ylabel("Average Marks")

plt.show()



# Q24: Marks ko bins me divide karke graph banao

# Ranges:
# 0–40
# 40–60
# 60–80
# 80–100

# Goal:
# Check karo → kaunsi range me sabse zyada students hain

bins = [0,40,60,80 ,100]
labels = ["0-40", "40-60", "60-80", "80-100"]
df["Marks_range"] = pd.cut(df["Marks"] , bins = bins , labels = labels)
range_count = df["Marks_range"].value_counts()
range_count.plot(kind = "bar" , color = "purple")

plt.title("Marks Distribution by Range")
plt.xlabel("Marks Range")
plt.ylabel("Number of Students")

plt.show()