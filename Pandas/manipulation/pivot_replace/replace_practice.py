import pandas as pd

# =====================
# REPLACE PRACTICE
# =====================

df = pd.DataFrame({
    "Name": ["A", "B", "C", "D"],
    "Gender": ["M", "F", "M", "F"]
})

print("Original Data:\n")
print(df)

# Replace values
df["Gender"] = df["Gender"].replace({
    "M": "Male",
    "F": "Female"
})

print("\nAfter Replace:\n")
print(df)



# =====================
# REPLACE WITH NUMBERS
# =====================

df = pd.DataFrame({
    "Name": ["A", "B", "C", "D"],
    "Result": ["Pass", "Fail", "Pass", "Fail"]
})

print("Original Data:\n")
print(df)

# Replace text with numbers
df["Result"] = df["Result"].replace({
    "Pass": 1,
    "Fail": 0
})

print("\nAfter Replace:\n")
print(df)