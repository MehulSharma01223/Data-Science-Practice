import pandas as pd
import matplotlib.pyplot as plt

# # Data load
df = pd.DataFrame({
    "Name": ["A","B","C","D","E","F","G","H","I","J"],
    "City": ["Delhi","Mumbai","Delhi","Pune","Chennai","Delhi","Mumbai","Pune","Chennai","Delhi"],
    "Marks": [80, 55, 90, 40, 70, 85, 60, 30, 75, 65],
    "Age": [21,22,23,20,22,24,23,21,22,20]
})

df["Result"] = df["Marks"].apply(lambda x: "Pass" if x > 60 else "Fail")

print(df)

#  Q .)  Marks category:
# >80 → Excellent
# >60 → Good
# else → Average

def category(x):
    if x > 80:
        return "Excellent"
    elif x > 60:
        return "Good"
    else:
        return "Average"

df["Category"] = df["Marks"].apply(category)

print(df)


# Age ke basis pe group banao:
# <23 → Young
# >=23 → Old

df["Group"] = df["Age"].apply(lambda x: "Young" if x < 23 else "Old")

print(df)