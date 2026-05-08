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



#  \\\\\\\\\\\\ D Types \\\\\\\\\\\\\\\\\\\\\\\\

# --------------- Q13. --------------------

# Check data types of all columns in the dataset

print(df.dtypes)

#  ---------------Q14.-------------------

# Check data type of only the Employee_ID column

print(df["Employee_ID"].dtypes)

# ----------------- Q15. -----------------

# Count how many columns are present for each data type

print(df.dtypes.value_counts())

#  -----------------Q16. ---------------

# Show only columns that have object data type

print(df.dtypes[df.dtypes == "object"])


#  -----------------Q17. ---------------

# Show only columns that have mumeric data type

print(df.dtypes[df.dtypes != "object"])


#  \\\\\\\\\\\\ astypes \\\\\\\\\\\\\\\\\\\\\\\\

#  --------------Q18. -------------

# Convert Employee_ID to string

df["Employee_ID"] = df["Employee_ID"].astype("str")

#  --------------Q19.-------------

# Convert Salary to float
df["Salary"] = df["Salary"].astype("float")

#  --------------Q19.-------------

# Convert Salary to int
df["Salary"] = df["Salary"].astype("int")

#  --------------Q20.--------------

# Convert Employee_ID column from integer to string type
# Permanently update the dataset

df["Employee_ID"] = df["Employee_ID"].astype("str")
print(df.dtypes)

# ------------  Q21. ---------------

# Convert Employee_ID column back to integer type
# Permanently update the dataset

df["Employee_ID"] = df["Employee_ID"].astype("int")
print(df.dtypes)

# ----------- Q.22 ------------

# Convert Employee_ID and Experience columns to float type
# Permanently update the dataset
 
df[["Employee_ID", "Experience"]] = df[["Employee_ID", "Experience"]].astype("float")
print(df.dtypes)

# ----------- Q.23 ------------

# Check data types after converting Employee_ID and Experience columns to float

print(df[["Employee_ID", "Experience"]].dtypes)

# ------------ Q 24. ----------

# Convert Name column to string type
# Permanently update the dataset

df["Name"] = df["Name"].astype("str")
print(df["Name"].dtypes)

#  ------------ Q 25. ----------

# Convert Employee_ID column to boolean type
# Check the output after conversion

df["Employee_ID"] = df["Employee_ID"].astype("bool")
print(df["Employee_ID"].dtypes)