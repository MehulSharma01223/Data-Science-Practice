import pandas as pd

data = {
    "Name": ["Aman", "Rahul", "Priya", "Neha"],
    "Age": [21, 23, 20, 22],
    "Marks": [85, 60, 90, 70]
}

df = pd.DataFrame(data)

# Select specific names
print(df[df["Name"].isin(["Aman", "Neha"])])

# Marks between 70 and 90
print(df[df["Marks"].between(70, 90)])


#  Query type
print(df.query("Marks > 70 and Age < 23"))
