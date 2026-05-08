import pandas as pd

df = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 101, 104, 102],
    "Name": ["Aman", "Riya", "Karan", "Aman", "Meena", "Riya"],
    "Department": ["HR", "IT", "Finance", "HR", "HR", "IT"]
})

print(df)

# ---------- Q1.-----------
# Detect duplicate rows in the dataset

print(df.duplicated())

# ---------------Q2.------------------

# Count total duplicate rows in the dataset
print(df.duplicated().sum())

# -------------Q3. ------------

# Show only duplicate rows from the dataset
print(df[df.duplicated()])

# ------------Q4. --------------

# Detect duplicate Employee_ID values only]
print(df.duplicated(subset = ["Employee_ID"]))

# ------------Q5.-----------

# Show rows where Employee_ID is duplicated
print(df[df.duplicated(subset = ["Employee_ID"])])
