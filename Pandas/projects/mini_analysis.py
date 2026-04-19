import pandas as pd

df = pd.DataFrame({
    "Name": ["A","B","C","D","E","F","G","H"],
    "City": ["Delhi","Mumbai","Delhi","Pune","Chennai","Delhi","Mumbai","Pune"],
    "Marks": [80, 55, 90, 40, 70, 85, 60, 30],
    "Age": [21,22,23,21,22,23,24,21]
})

df.to_csv(r"C:\Users\MAINAK\Desktop\SQl\datasets\sample_data.csv", index=False)
print("CSV Created")

df = pd.read_csv(r"C:\Users\MAINAK\Desktop\SQl\datasets\sample_data.csv")
print(df)

# Highest marks wala student nikaal

topper = df.sort_values(by = "Marks",ascending= False).head(1)
print("Topper: \n",topper)
mead = df["Marks"].mean()
print(mead)

city_counts = df["City"].value_counts()
print(city_counts)

# # Marks < 50 walon ko 0 replace karo (loc use karo)
df.loc[df["Marks"]<50 , "Marks"] = 0
print(df)

# City = Delhi
# Marks > 60
# descending sort

result = df[(df["City"] == "Delhi") & (df["Marks"] > 60)]\
            .sort_values(by="Marks" , ascending= False)

print(result)

# Mumbai aur Pune hatao
# Marks > 50
# sirf Name aur Marks dikhao

result = df[(~df["City"].isin(["Pune","Mumbai"])) & (df["Marks"] > 60) ]\
            [["Name","Marks"]]
print(result)

# Marks ke basis pe top 3 students
top3 = df.sort_values(by = "Marks" , ascending=False).head(3)
print("3 topper in the class :\n ", top3)

# Age < 23
# Marks descending sort
young = df[df["Age"] < 23].sort_values(by = "Marks" , ascending=False)
print("Young Students : \n",young)


# Delhi + Chennai students
# Marks > 60
# descending sort
# top 2

result = df[(df["City"].isin(["Delhi" , "Chennai"])) & (df["Marks"] >60)]\
            .sort_values(by = "Marks" , ascending= False).head(2)
print(result)