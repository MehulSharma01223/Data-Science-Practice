import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 104, 105, 106, 107, 108],

    "Name": ["Aman", "Riya", np.nan, "Karan", "Meena", "Rohit", np.nan, "Simran"],

    "Department": ["HR", "IT", "Finance", np.nan, "HR", "IT", "Finance", "HR"],

    "Salary": [45000, np.nan, 52000, 48000, np.nan, 61000, 57000, 49000],

    "Experience": [2, 5, np.nan, 3, 4, np.nan, 6, 2],

    "City": ["Delhi", "Mumbai", "Pune", np.nan, "Jaipur", "Delhi", np.nan, "Kota"],

    "Performance_Score": [8.5, 9.1, np.nan, 7.0, 8.2, 9.5, 6.8, np.nan]
})

print(df)

# -------------------------------- Q 1 . -------------------------
# HR analytics team needs employee salary data for payroll analysis
# Remove rows where Salary is missing
# Store cleaned result in salary_df

salary_df = df.dropna(subset = ["Salary"])
print(salary_df)

# --------------------------------Q2. ----------------------------

# Employee performance analysis requires Performance_Score
# Fill missing Performance_Score values with the average score
# Permanently update the dataset

df["Performance_Score"] = df["Performance_Score"].fillna(df["Performance_Score"].mean())
print(df)


# ----------------------------Q3.----------------------

# City information is important for regional employee reporting
# Permanently remove rows where City is missing

df.dropna(subset = ["City"] ,inplace = True)
print(df)

#  -------------------------Q4. -----------------------

# HR team found that some employees have missing Name values
# Replace missing Name values with "Unknown Employee"
# Permanently update the dataset

df["Name"] = df["Name"].fillna("Unknown Employee")
print(df)

# --------------------------Q5. ---------------------

# Finance department only wants employees with Salary and Performance_Score available
# Remove rows where either Salary or Performance_Score is missing
# Store cleaned result in finance_df

finance_df = df.dropna(subset=["Salary", "Performance_Score"])
print(finance_df)

#  ------------------------ Q6. -------------------------

# HR dashboard requires at least 5 non-null values in every employee record
# Remove rows that contain less than 5 non-null values
# Store cleaned result in hr_df

hr_df = df.dropna(thresh= 5)
print(hr_df)

#  ----------------------- Q7. --------------------------

# IT department wants only records where Department and City are both available
# Remove rows where either Department or City is missing
# Store cleaned result in it_df

it_df =df.dropna(subset = ["Department" , "City"])
print(it_df)

# -------------------------------Q8. ----------------------

# Employee experience data is required for promotion analysis
# Fill missing Experience values with the average experience
# Permanently update the dataset

df["Experience"] = df["Experience"].fillna(df["Experience"].mean())
print(df)

# ------------------- Q9. -----------------------------

# Management only wants employees with complete records
# Remove all rows that contain any missing values
# Store cleaned result in final_df

final_df = df.dropna()
print(final_df)

# ------------------Q10. ---------------------------

# HR team wants to know how many employee records were removed after cleaning
# Compare total rows before and after using dropna()

compare_total = len(df) - len(final_df)
print(compare_total)