import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 101, 104, 105, 102, 106],

    "Name": ["Aman", "Riya", np.nan, "Aman", "Meena", "Rohit", "Riya", "Simran"],

    "Department": ["HR", "IT", "Finance", "HR", np.nan, "IT", "IT", "Finance"],

    "Salary": [45000, np.nan, 52000, 45000, 61000, 58000, np.nan, 72000],

    "Experience": [2, 5, np.nan, 2, 7, 4, 5, np.nan],

    "City": ["Delhi", "Mumbai", "Pune", "Delhi", np.nan, "Delhi", "Mumbai", "Kota"],

    "Performance_Score": [8.5, 9.1, np.nan, 8.5, 7.8, 8.9, 9.1, 6.5]
})

print(df)


# --------- QUESTION 1--------

# HR analytics team found duplicate employee records
# Remove duplicate Employee_ID entries
# Keep only the first occurrence
# Store cleaned result in hr_df

hr_df = df.drop_duplicates(subset= ["Employee_ID"] , keep= "first") 
print(hr_df)

# --------- QUESTION 2 ----------

# Finance team requires Salary data for payroll processing
# Remove rows where Salary is missing
# Store cleaned result in finance_df

finance_df = df.dropna(subset=["Salary"])
print(finance_df)

# ------------ QUESTION 3 ----------

# Employee records with missing Name values are invalid
# Replace missing Name values with "Unknown Employee"
# Permanently update the dataset

df["Name"] = df["Name"].fillna("Unknown Employee")
print(df)

# --------- QUESTION 4 --------

# Management only wants employee records with complete data
# Remove all rows that contain any missing values
# Store cleaned result in final_df

Final_df = df.dropna()
print(Final_df)

# ------------ QUESTION 5 -----------

# HR team wants to remove completely repeated employee records
# Permanently remove duplicate rows from the dataset

df.drop_duplicates(inplace= True)
print(df)

# -------- QUESTION 6 ------------

# Employee performance analysis requires at least 5 non-null values in every row
# Remove rows with less than 5 non-null values
# Store cleaned result in performance_df

performance_df = df.dropna(thresh= 5)
print(performance_df)

# ----------- QUESTION 7 ---------

# IT department wants only unique employee records based on Employee_ID
# Remove duplicate Employee_ID values
# Keep only the latest record
# Store cleaned result in it_df

it_df = df.drop_duplicates(subset = ["Employee_ID"] , keep = "last")
print(it_df)

# ------- QUESTION 8 --------

# HR dashboard only needs employees where Department and City are both available
# Remove rows where either Department or City is missing
# Store cleaned result in dashboard_df

dashboard_df = df.dropna(subset = ["Department" , "City"])
print(dashboard_df)

# --------- QUESTION 9----------

# Company wants to completely remove duplicate Employee_ID records
# Do not keep any repeated Employee_ID values
# Store cleaned result in unique_df

unique_df = df.drop_duplicates(subset = ["Employee_ID"] , keep = False)
print(unique_df)

# ----------- QUESTION 10 --------

# HR team wants to know how many duplicate Employee_ID records exist
# Count total duplicate Employee_ID values in the dataset

df.duplicated(subset = ["Employee_ID"]).sum()
