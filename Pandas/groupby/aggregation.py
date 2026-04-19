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

