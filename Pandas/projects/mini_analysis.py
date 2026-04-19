import pandas as pd

# =====================
# Load Data
# =====================

df = pd.DataFrame({
    "Name": ["A","B","C","D","E","F","G","H"],
    "City": ["Delhi","Mumbai","Delhi","Pune","Chennai","Delhi","Mumbai","Pune"],
    "Marks": [80, 55, 90, 40, 70, 85, 60, 30],
    "Age": [21,22,23,21,22,23,24,21]
})

# =====================
# Data Cleaning
# =====================

# Marks < 50 → replace with 0
df.loc[df["Marks"] < 50, "Marks"] = 0

# =====================
# Analysis 1: Topper
# =====================

topper = df.sort_values(by="Marks", ascending=False).head(1)
print("Topper:\n", topper)

# =====================
# Analysis 2: City-wise Summary
# =====================

city_analysis = df.groupby("City")["Marks"].agg(["mean","max","min"])
print("\nCity-wise Marks Analysis:\n", city_analysis)

# =====================
# Analysis 3: Top 3 Students
# =====================

top3 = df.sort_values(by="Marks", ascending=False).head(3)
print("\nTop 3 Students:\n", top3)

# =====================
# Analysis 4: High Performers (>60)
# =====================

high_perf = df[df["Marks"] > 60].groupby("City").size()
print("\nHigh Performers (>60):\n", high_perf)

# =====================
# Analysis 5: Young Students (<23)
# =====================

young = df[df["Age"] < 23].sort_values(by="Marks", ascending=False)
print("\nYoung Students:\n", young)

# =====================
# Analysis 6: Topper per City
# =====================

city_topper = df.loc[df.groupby("City")["Marks"].idxmax()]
print("\nCity-wise Topper:\n", city_topper)

# =====================
# Analysis 7: Performance Category
# =====================

avg_marks = df.groupby("City")["Marks"].mean()

def category(x):
    if x > 75:
        return "Good"
    elif x > 60:
        return "Average"
    else:
        return "Poor"

performance = avg_marks.apply(category)
print("\nPerformance Category:\n", performance)

# =====================
# INSIGHTS
# =====================

print("\nINSIGHTS:")

print("1. Delhi has the highest average marks, indicating strong performance.")
print("2. Mumbai shows lower performance compared to other cities.")
print("3. Most top-performing students belong to Delhi.")
print("4. Pune has low marks indicating weaker performance.")
print("5. Overall, Delhi falls under 'Good' category based on average marks.")