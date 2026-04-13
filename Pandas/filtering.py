import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    "Name": ["A", "B", "C", "D", "E"],
    "Marks": [80, 45, 90, 60, 30],
    "Age": [20, 21, 19, 18, 22]
})

# Q1: Filter Marks > 50
print(df[df["Marks"] > 50])

# Q2: Filter Marks > 50 AND Age < 21
print(df[(df["Marks"] > 50) & (df["Age"] < 21)])

# Q3: Filter Marks < 50 OR Age > 20
print(df[(df["Marks"] < 50) | (df["Age"] > 20)])

# Q4: Select only Name and Marks where Marks > 60
print(df.loc[df["Marks"] > 60, ["Name", "Marks"]])

# Q5: Find students with Marks between 50 and 90
print(df[(df["Marks"] >= 50) & (df["Marks"] <= 90)])
