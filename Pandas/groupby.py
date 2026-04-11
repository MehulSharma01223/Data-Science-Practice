import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    "Dept": ["IT", "HR", "IT", "HR", "Sales", "Sales"],
    "Name": ["A", "B", "C", "D", "E", "F"],
    "Salary": [50000, 40000, 60000, 45000, 30000, 35000]
})

# Q1: Average salary per department
print(df.groupby("Dept")["Salary"].mean())

# Q2: Total salary per department
print(df.groupby("Dept")["Salary"].sum())

# Q3: Count employees per department
print(df.groupby("Dept")["Name"].count())

# Q4: Multiple aggregation
print(df.groupby("Dept")["Salary"].agg(["mean", "max", "min"]))

# Q5: Group by Dept and show full data
print(df.groupby("Dept")[["Salary"]].sum())
