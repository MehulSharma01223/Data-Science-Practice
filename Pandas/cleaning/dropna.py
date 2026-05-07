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
print(df)