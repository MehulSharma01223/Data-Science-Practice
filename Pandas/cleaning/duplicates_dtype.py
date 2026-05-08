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

#  -----------Q6. ------------

# Remove duplicate rows from the dataset
df_duplicates   = df.drop_duplicates()

# ------------Q7. ----------

# Count total rows after removing duplicates

sount_total = len(df)- len(df_duplicates)
print(sount_total)

#  -----------Q8. ----------

# Remove duplicate Employee_ID records only

print(df.drop_duplicates(subset = ["Employee_ID"]))

#  ----------- Q9. ----------

# Keep only the last duplicate record of Employee_ID

df.drop_duplicates(subset=["Employee_ID"], keep="last")

#  -----------Q10. ------------

# Remove all duplicate Employee_ID records completely
# Do not keep any repeated IDs

print(df.drop_duplicates(subset=["Employee_ID"], keep=False))

#  -----------Q11.----------

# Permanently remove duplicate Employee_ID records from the dataset
df.drop_duplicates(subset=["Employee_ID"], inplace= True)
print(df)

# -------------Q12.--------

# Count total duplicate Employee_ID values in the dataset
print(df.duplicated(subset = ["Employee_ID"]).sum())
