import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["A", "B", "C", "D", np.nan],
    "Marks": [80, np.nan, 70, 60, 90],
    "City": ["Delhi", "Mumbai", np.nan, "Pune", "Delhi"]
})

print(df)

#  Check all missing values
print(df.isnull())

# Count missing values
print(df.isnull().sum())

# Check missing values only in City
print(df["City"].isnull())

# Count total missing values in dataset
print(df.isnull().sum().sum()) 

# Sirf un rows ko identify karo jaha missing value present hai.

df[df.isnull().any(axis = 1)]