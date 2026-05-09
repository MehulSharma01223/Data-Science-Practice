import pandas as pd

df = pd.read_csv(r"C:\Users\MAINAK\Desktop\SQl\Pandas\projects\employee_analytics\data\employee_data.csv")

print("Dataset Loaded Successfully")
print(df)

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Data Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Fill missing Name values
df["Name"] = df["Name"].fillna("Unknown Employee")

# Fill missing Department values
df["Department"] = df["Department"].fillna("Unknown")

# Fill missing Salary values with average salary
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# Fill missing Experience values with average experience
df["Experience"] = df["Experience"].fillna(df["Experience"].mean())

# Fill missing City values
df["City"] = df["City"].fillna("Unknown")

# Fill missing Performance_Score values with average score
df["Performance_Score"] = df["Performance_Score"].fillna(df["Performance_Score"].mean())

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDuplicate Rows Before Cleaning:")
print(df.duplicated().sum())

# Remove duplicate Employee_ID records
df.drop_duplicates(subset=["Employee_ID"], inplace=True)

print("\nDuplicate Rows After Cleaning:")
print(df.duplicated().sum())

print("\nData Types Before Fixing:")
print(df.dtypes)

# Convert Employee_ID to string
df["Employee_ID"] = df["Employee_ID"].astype("str")

# Convert Experience to integer
df["Experience"] = df["Experience"].astype("int")

print("\nData Types After Fixing:")
print(df.dtypes)

print("\nAverage Salary:")
print(df["Salary"].mean())

print("\nHighest Salary:")
print(df["Salary"].max())

print("\nLowest Salary:")
print(df["Salary"].min())

print("\nDepartment-wise Average Salary:")
print(df.groupby("Department")["Salary"].mean())

print("\nCity-wise Employee Count:")
print(df["City"].value_counts())

print("\nTop 3 Highest Paid Employees:")
print(df.sort_values(by="Salary", ascending=False).head(3))

import matplotlib.pyplot as plt

# Department-wise Average Salary
dept_salary = df.groupby("Department")["Salary"].mean()

plt.figure(figsize=(8,5))

plt.bar(dept_salary.index, dept_salary.values)

plt.title("Department-wise Average Salary")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.savefig("visuals/department_salary.png")

plt.close()

city_count = df["City"].value_counts()

plt.figure(figsize=(8, 5))

plt.bar(city_count.index, city_count.values)

plt.title("City-wise Employee Count")
plt.xlabel("City")
plt.ylabel("Number of Employees")

plt.savefig("visuals/city_employee_count.png")

plt.close()

plt.figure(figsize=(8,5))

plt.hist(df["Performance_Score"], bins=5)

plt.title("Employee Performance Score Distribution")
plt.xlabel("Performance Score")
plt.ylabel("Number of Employees")

plt.savefig("visuals/performance_distribution.png")

plt.close()

plt.figure(figsize=(8,5))

plt.scatter(df["Salary"], df["Performance_Score"])

plt.title("Salary vs Performance Score")
plt.xlabel("Salary")
plt.ylabel("Performance Score")

plt.savefig("visuals/salary_vs_performance.png")

plt.close()

# -------------------------------
# Top 5 Highest Paid Employees
# -------------------------------

top_salary = df.sort_values(by="Salary", ascending=False).head(5)

plt.figure(figsize=(8,5))

plt.bar(top_salary["Name"], top_salary["Salary"])

plt.title("Top 5 Highest Paid Employees")
plt.xlabel("Employee Name")
plt.ylabel("Salary")

plt.savefig("visuals/top5_salary.png")

plt.close()


# -------------------------------
# Department Employee Distribution
# -------------------------------

dept_count = df["Department"].value_counts()

plt.figure(figsize=(7,7))

plt.pie(
    dept_count.values,
    labels=dept_count.index,
    autopct="%1.1f%%"
)

plt.title("Department Employee Distribution")

plt.savefig("visuals/department_distribution.png")

plt.close()


# -------------------------------
# Experience Distribution
# -------------------------------

plt.figure(figsize=(8,5))

plt.hist(df["Experience"], bins=5)

plt.title("Employee Experience Distribution")
plt.xlabel("Years of Experience")
plt.ylabel("Number of Employees")

plt.savefig("visuals/experience_distribution.png")

plt.close()


# -------------------------------
# Average Performance by Department
# -------------------------------

dept_perf = df.groupby("Department")["Performance_Score"].mean()

plt.figure(figsize=(8,5))

plt.bar(dept_perf.index, dept_perf.values)

plt.title("Average Performance by Department")
plt.xlabel("Department")
plt.ylabel("Average Performance Score")

plt.savefig("visuals/department_performance.png")

plt.close()