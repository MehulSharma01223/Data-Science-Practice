import pandas as pd 
import numpy as np

import pandas as pd

# Dictionary se DataFrame
data = {
    "Name": ["Aman", "Rahul", "Priya"],
    "Age": [21, 23, 20],
    "Marks": [85, 90, 88]
}

df = pd.DataFrame(data)

print(df)

#  Single line access

print(df["Name"])

# multple line access

print(df [["Name"],["Marks"]])

#  add new line

df["pass"] = df["Maarks"]>80
print(df)

#  Modify Column
df["Marks"] = df["Marks"] + 5

#  delete Column

df.drop("Age",axis = 1 , inplace= True)
