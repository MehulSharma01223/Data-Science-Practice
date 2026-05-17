import pandas as pd

# =====================
# RIGHT MERGE
# =====================

students_right = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["A", "B", "C"]
})

marks_right = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Marks": [80, 90, 70, 100]
})

print("RIGHT MERGE:\n")

print(pd.merge(students_right, marks_right, how="right"))

# =====================
# OUTER MERGE
# =====================

students_outer = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["A", "B", "C"]
})

marks_outer = pd.DataFrame({
    "ID": [1, 2, 4],
    "Marks": [80, 90, 100]
})

print("\nOUTER MERGE:\n")

print(pd.merge(students_outer, marks_outer, how="outer"))