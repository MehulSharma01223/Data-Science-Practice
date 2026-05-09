import pandas as pd

df = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 101, 104, 102],
    "Name": ["Aman", "Riya", "Karan", "Aman", "Meena", "Riya"],
    "Department": ["HR", "IT", "Finance", "HR", "HR", "IT"]
})

print(df)

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

# INDUSTRY QUESTION 1
# HR reporting system requires Employee_ID as string type
# Convert Employee_ID column to string
# Permanently update the dataset

df["Employee_ID"] = df["Employee_ID"].astype("str")


# INDUSTRY QUESTION 2
# Payroll analysis requires Salary column in float format
# Convert Salary column to float type
# Permanently update the dataset
df["Salary"] = df["Salary"].astype("float")


# INDUSTRY QUESTION 3
# Company wants Experience column in integer format
# Convert Experience column to integer type
# Permanently update the dataset

df["Experience"] = df["Experience"].fillna(0).astype("int")


# INDUSTRY QUESTION 4
# Reporting dashboard requires Employee_ID and Salary in string format
# Convert both columns to string type together
# Permanently update the dataset

df[["Employee_ID", "Salary"]] = df[["Employee_ID", "Salary"]].astype("str")

# INDUSTRY QUESTION 5
# Employee active status needs boolean format
# Convert Employee_ID column to boolean type
# Observe the output after conversion

df["Employee_ID"] = df["Employee_ID"].astype("bool")
