import pandas as pd

# =====================
# ROW CONCAT
# =====================

df1 = pd.DataFrame({
    "Name": ["A", "B"]
})

df2 = pd.DataFrame({
    "Name": ["C", "D"]
})

result = pd.concat([df1, df2] , ignore_index=  True)

print(result)

df1 = pd.DataFrame({
    "Name": ["A", "B"]
})

df2 = pd.DataFrame({
    "Marks": [80, 90]
})
result = pd.concat([df1, df2], axis=1)

print(result)