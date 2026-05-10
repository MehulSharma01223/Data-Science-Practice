import pandas as pd

# =====================
# DIFFERENT COLUMN NAMES
# =====================

students = pd.DataFrame({
    "Student_ID": [1, 2, 3],
    "Name": ["A", "B", "C"]
})

marks = pd.DataFrame({
    "ID": [1, 2, 3],
    "Marks": [80, 90, 70]
})

print("Students:\n")
print(students)

print("\nMarks:\n")
print(marks)

# =====================
# MERGE USING left_on & right_on
# =====================

result = pd.merge(
    students,
    marks,
    left_on="Student_ID",
    right_on="ID"
)

print("\nMERGED DATA:\n")
print(result)