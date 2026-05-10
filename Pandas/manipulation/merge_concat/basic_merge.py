import pandas as pd

# =====================
# INNER MERGE
# =====================

students_inner = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["A", "B", "C"]
})

marks_inner = pd.DataFrame({
    "ID": [1, 2, 3],
    "Marks": [80, 90, 70]
})

print("INNER MERGE:\n")

print(pd.merge(students_inner, marks_inner))

# =====================
# LEFT MERGE
# =====================

students_left = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Name": ["A", "B", "C", "D"]
})

marks_left = pd.DataFrame({
    "ID": [1, 2, 3],
    "Marks": [80, 90, 70]
})

print("\nLEFT MERGE:\n")

print(pd.merge(students_left, marks_left, how="left"))