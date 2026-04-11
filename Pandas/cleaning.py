import pandas as pd
import numpy as np

# Sample DataFrame with missing values
df = pd.DataFrame({
    "Name": ["A", "B", "C", "D", "E"],
    "Marks": [80, np.nan, 90, None, 60],
    "Age": [20, 21, None, 19, np.nan]
})

# Q1: Check missing values
print(df.isnull())

# Q2: Count missing values per column
print(df.isnull().sum())

# Q3: Drop rows with missing values
print(df.dropna())

# Q4: Fill missing values with constant
print(df.fillna(0))

# Q5: Fill missing Marks with mean
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
print(df)

# Q6: Forward fill
print(df.fillna(method="ffill"))

# Q7: Backward fill
print(df.fillna(method="bfill"))
