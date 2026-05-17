import pandas as pd

data = {
    "Name": ["Aman", "Rahul", "Priya", "Neha"],
    "Age": [21, 23, 20, 22],
    "Marks": [85, 60, 90, 70]
}

df = pd.DataFrame(data)

# Marks > 80
print(df[df["Marks"] > 80])

#  Multiple conditions

# Marks > 70 AND Age < 23
filtered = df[(df["Marks"] > 70) & (df["Age"] < 23)]

print(filtered)

#  OR  conditions

# Marks < 65 OR Age > 22
print(df[(df["Marks"] < 65) | (df["Age"] > 22)])

#  specofoc column filtter
print(df[df["Marks"] > 70][["Name", "Marks"]])
