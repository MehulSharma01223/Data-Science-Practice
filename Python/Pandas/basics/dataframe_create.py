import pandas as pd
import numpy as np

# Dictionary se DataFrame
data = {
    "Name": ["Aman", "Rahul", "Priya"],
    "Age": [21, 23, 20],
    "Marks": [85, 90, 88]
}

df = pd.DataFrame(data)

print(df)

print(df.shape)     # (rows, columns)
print(df.columns)   # column names
print(df.index)     # row numbers
print(df.dtypes)    # data types
print(df.values)    # numpy array
print(df.head())   # first 5 rows
print(df.tail())   # last 5 rows
print(df.info())   # full summary
print(df.describe())  # stats (mean, min, max)