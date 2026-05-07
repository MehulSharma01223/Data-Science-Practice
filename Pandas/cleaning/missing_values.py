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



# Q1. Marks ya City me missing value wali rows print karo
print(df[df[["Marks" , "City"]].isnull().any(axis = 1)])

# Q2. Har row me kitni missing values hain, new column banao

df["Missing_Count"] = df.isnull().sum(axis=1)

print(df)

#  Q3. Sirf missing values wale columns print karo

print(df.columns[df.isnull().sum() > 0])

# Q4. Har column ka missing percentage nikalo

print((df.isnull().sum() / len(df)) * 100)


# #   FILL NA

#  with num 
print(df.fillna(0))

#  with specific col
df["Marks"] = df["Marks"].fillna(0)
print(df)

#  with mean()

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
print(df)
#  with string 

print(df.fillna("Unknown"))


# Q1

# Name column ki missing value ko "No Name" se fill karo.

df["Name"].fillna("No Name ")

# Q2

# City column ki missing value ko "Unknown" se fill karo.
df["City"].fillna("Unknown")

# Q3

# Marks column ki missing value ko Marks ke mean se fill karo.
df["Marks"].fillna(df["Marks"].mean())

# Q4

# Ek new dataframe banao:

df_filled = df.fillna({
    "Name": "No Name",
    "Marks": df["Marks"].mean(),
    "City": "Unknown"
})

print(df_filled)

# Q5.

# Check karo: df_filled me abhi bhi missing values bachi hain ya nahi.

print(df_filled.isnull().sum())

# #  Q6.
# Marks column me missing value ko mean se fill karo, phir uske baad Marks ka average dubara print karo.

print(df["Marks"].mean())

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print(df["Marks"].mean())
