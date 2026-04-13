import pandas as pd

# Q1: Create a DataFrame
df = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Marks": [80, 90, 70]
})
print(df)

# Q2: Select column
print(df["Marks"])

# Q3: Filter Marks > 75
print(df[df["Marks"] > 75])

# Q4: Show first rows
print(df.head())

# Q5: Add new column
df["Status"] = df["Marks"] > 75
print(df)



#  Q. Create a DataFrame with Name and Marks
#  Print entire DataFrame
#  Print only Marks column 

import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "Name": ["Aman", "Riya", "Rahul", "Neha"],
    "Marks": [85, 90, 78, 92]
})

# Print entire DataFrame
print(df)

# Print only Marks column
print(df["Marks"])
