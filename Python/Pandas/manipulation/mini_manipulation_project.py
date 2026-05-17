import pandas as pd

# =====================
# EMPLOYEE DETAILS
# =====================

employees = pd.DataFrame({
    "Emp_ID": [101, 102, 103, 104, 105],
    "Name": ["Rahul", "Priya", "Aman", "Sneha", "Karan"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "City": ["Delhi", "Mumbai", "Pune", "Delhi", "Mumbai"]
})

print("EMPLOYEES:\n")
print(employees)

# =====================
# SALARY DETAILS
# =====================

salary = pd.DataFrame({
    "Emp_ID": [101, 102, 103, 104, 105],
    "Salary": [70000, 50000, 80000, 65000, 55000],
    "Performance": ["Good", "Average", "Excellent", "Good", "Average"]
})

print("\nSALARY DATA:\n")
print(salary)

result = pd.merge(employees, salary, on="Emp_ID")

print(result)

city_codes = {
    "Delhi": "DL",
    "Mumbai": "MH",
    "Pune": "PN"
}

result["City_Code"] = result["City"].map(city_codes)

print(result)

result["Performance_Score"] = result["Performance"].replace({
    "Excellent": 3,
    "Good": 2,
    "Average": 1
})

print(result)

pivot = pd.pivot_table(
    result,
    values=["Salary", "Performance_Score"],
    index="Department",
    aggfunc="mean"
)

print("\nDEPARTMENT REPORT:\n")

print(pivot)