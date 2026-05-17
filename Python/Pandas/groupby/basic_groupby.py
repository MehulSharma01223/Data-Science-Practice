import pandas as pd

df = pd.DataFrame({
    "Name": ["A","B","C","D","E","F"],
    "City": ["Delhi","Pune","Delhi","Mumbai","Mumbai","Delhi"],
    "Marks": [80, 60, 90, 70, 50, 85],
    "Age": [21,22,23,21,22,23]
})

# Group by City
grp = df.groupby("City")

print(grp)
# Q1: City-wise average Marks
# Q2: City-wise maximum Marks
# Q3: City-wise minimum Marks
print(df.groupby("City")["Marks"].mean())
print(df.groupby("City")["Marks"].max())
print(df.groupby("City")["Marks"].min())

# Q4: City-wise Marks ka sum
# Q5: City-wise student count
# Q6: City-wise Age ka average (agar Age column ho)
print(df.groupby("City")["Marks"].sum())
print(df.groupby("City")["Name"].count())
print(df.groupby("City")["Age"].mean())

# Q7: Har city ka topper nikaal
# Q8: Har city ka lowest scorer nikaal
# Q9: Sirf Delhi aur Mumbai ka group bana ke average nikaal
print(df.groupby("City").max().head(1))
print(df.groupby("City").min().tail(1))
result = df[df["City"].isin(["Delhi" , "Mumbai"])]\
            .groupby("City")["Marks"].mean()
print(result)
