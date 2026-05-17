import pandas as pd

# =====================
# PIVOT TABLE PRACTICE
# =====================

df = pd.DataFrame({
    "Name": ["A", "B", "C", "D"],
    "City": ["Delhi", "Delhi", "Mumbai", "Mumbai"],
    "Marks": [80, 90, 70, 60]
})

pivot = pd.pivot_table(
    df,
    values="Marks",
    index="City",
    aggfunc="mean"
)

print(pivot)