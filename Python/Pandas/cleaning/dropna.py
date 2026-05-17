import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["A", "B", "C", "D", np.nan],
    "Marks": [80, np.nan, 70, 60, 90],
    "City": ["Delhi", "Mumbai", np.nan, "Pune", "Delhi"]
})


#  Q1.  jitni bhi rows me missing values hain
# unhe remove karo.

print(df.dropna())

# Marks whale missing value delete kar 

print(df.dropna(subset=["Marks"]))


# city aur Name whale missing value delete kar 

print(df.dropna(subset=["Marks" , "Name"]))

# Dataset me:

# jitni rows me missing values hain
# unhe permanently remove karo.

# Aur updated dataframe print karo.

print(df.dropna(inplace=True))


# Q1 . Sirf un rows ko remove karo:

print(df.dropna(subset = ["Name" , "Marks"] , how = "all"))

# HARD Q2
# Remove rows that have less than 2 non-null values
print(df.dropna(thresh=2))

# HARD Q3
# Remove rows where Marks contains missing values
# Store the cleaned result in clean_df
# Original df should not change

clean_df = df.dropna(subset = ["Marks"])
print(clean_df)

# HARD Q4
# Find how many rows were removed after using dropna()
removed_rows = len(df) - len(clean_df)
print(removed_rows)

# HARD Q5
# Remove rows where all values are missing

print(df.dropna(how = "all"))

# HARD Q6
# Remove rows where Name, Marks, and City all contain missing values
print(df.dropna(subset = ["Marks" ,"Name","City"] ,how = "all"))

# HARD Q7
# Permanently remove rows where City contains missing values

df.dropna(subset = ["City"] ,inplace = True)
print(df)

# HARD Q8
# Remove rows where either Name or Marks contains missing values
print(df.dropna(subset = ["Marks" ,"Name"] ,how = "any"))

# HARD Q9
# Create a new dataframe that only keeps rows with no missing values

new_df = df.dropna()