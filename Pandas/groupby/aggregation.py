import pandas as pd

df = pd.DataFrame({
    "Name": ["A","B","C","D","E","F"],
    "City": ["Delhi","Pune","Delhi","Mumbai","Mumbai","Delhi"],
    "Marks": [80, 60, 90, 70, 50, 85],
    "Age": [21,22,23,21,22,23]
})

#  Easy level question for aggregarion 

# Q1: City-wise mean, max, min Marks (agg use karo)

print(df.groupby("City")["Marks"].agg(["mean","max","min"]))

# Q2: City-wise Marks ka sum aur count

print(df.groupby("City").agg({
     "Marks": ["sum","count"]
 }))

# Q3: City-wise Age ka min aur max

print(df.groupby("City")["Age"].agg(["min","max"]))




# Q4: City-wise → Marks (mean, max) + Age (mean)
print(df.groupby("City").agg({
    "Marks":["mean","max"],
    "Age":["mean"]
}))


# Q5: City-wise unique Names count (nunique use karo)
print(df.groupby("City")["Name"].nunique())

# Q6: City-wise → Marks sum + Age max
print(df.groupby("City").agg({
    "Marks" : ["sum"],
    "Age": ["max"]
}))



# Q7: Rename columns → avg_marks, max_marks

print(df.groupby("City").agg(
    avg_marks = ("Marks","mean"),
    max_marks = ("Marks","max")
))

# Q8: City-wise → Marks mean + Age min + Age max (custom agg)


print(df.groupby("City").agg({
    "Marks" : ["mean"],
    "Age" : ["min","max"]

}))


# Q9: Sirf Delhi & Mumbai → agg(mean, max)

result = df[df["City"].isin(["Delhi","Mumbai"])]\
            .groupby("City")["Marks"].agg(["mean","max"])
print(result)

# Q10: Har city ka topper (max Marks wala row)
topper = df.loc[df.groupby("City")["Marks"].idxmax()]
print(topper)

# Q11: Har city me kitne students 60 se upar hai
result = df[df["Marks"] > 60 ].groupby("City").size()
print(result)
# Q12: City-wise performance category banao:
#      mean > 75 → "Good"
#      mean > 60 → "Average"
#      else → "Poor"
avg = df.groupby("City")["Marks"].mean()

