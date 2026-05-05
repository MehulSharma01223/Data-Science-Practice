import pandas as pd
import matplotlib.pyplot as plt
import os

# =====================
# Paths
# =====================

DATA_PATH = r"C:\Users\MAINAK\Desktop\SQl\Pandas\projects\student_analysis\data\data.csv"
VISUALS_DIR = r"C:\Users\MAINAK\Desktop\SQl\Pandas\projects\student_analysis\visuals"
INSIGHTS_PATH = r"C:\Users\MAINAK\Desktop\SQl\Pandas\projects\student_analysis\insights.txt"

os.makedirs(VISUALS_DIR, exist_ok=True)

# =====================
# Load Data
# =====================

df = pd.read_csv(DATA_PATH)

# =====================
# Data Cleaning
# =====================

df.loc[df["Marks"] < 50, "Marks"] = 0

# =====================
# Analysis
# =====================

topper = df.sort_values(by="Marks", ascending=False).head(1)
top3 = df.sort_values(by="Marks", ascending=False).head(3)

city_analysis = df.groupby("City")["Marks"].agg(["mean", "max", "min"])
city_topper = df.loc[df.groupby("City")["Marks"].idxmax()]

high_students = df[df["Marks"] > 60].groupby("City").size()
total_students = df.groupby("City").size()
high_percentage = (high_students / total_students).fillna(0) * 100

city_total_marks = df.groupby("City")["Marks"].sum()

young_students = df[df["Age"] < 23]
old_students = df[df["Age"] >= 23]

df["Age_Group"] = df["Age"].apply(lambda x: "Young" if x < 23 else "Old")
age_group_avg = df.groupby("Age_Group")["Marks"].mean()

avg_marks = df.groupby("City")["Marks"].mean()

def performance_category(x):
    if x > 75:
        return "Good"
    elif x > 60:
        return "Average"
    else:
        return "Poor"

performance = avg_marks.apply(performance_category)
performance_count = performance.value_counts()

bins = [0, 40, 60, 80, 100]
labels = ["0-40", "40-60", "60-80", "80-100"]
df["Marks_Range"] = pd.cut(df["Marks"], bins=bins, labels=labels, include_lowest=True)
marks_range_count = df["Marks_Range"].value_counts().sort_index()

# =====================
# Visual 1: High Performers Percentage
# =====================

high_percentage.plot(kind="bar", color="orange")
plt.title("High Performers Percentage by City")
plt.xlabel("City")
plt.ylabel("Percentage (%)")
plt.tight_layout()
plt.savefig(os.path.join(VISUALS_DIR, "q16_high_performers_percentage.png"))
plt.close()

# =====================
# Visual 2: City-wise Total Marks Pie Chart
# =====================

city_total_marks.plot(kind="pie", autopct="%1.1f%%")
plt.title("City-wise Total Marks Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig(os.path.join(VISUALS_DIR, "q17_city_total_marks_pie.png"))
plt.close()

# =====================
# Visual 3: Marks vs Age Scatter Plot
# =====================

df.plot(x="Age", y="Marks", kind="scatter", color="blue")
plt.title("Marks vs Age")
plt.xlabel("Age")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig(os.path.join(VISUALS_DIR, "q18_marks_vs_age_scatter.png"))
plt.close()

# =====================
# Visual 4: Top 5 Students
# =====================

top5 = df.sort_values(by="Marks", ascending=False).head(5)
top5.plot(x="Name", y="Marks", kind="bar", color="pink")
plt.title("Top 5 Students by Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig(os.path.join(VISUALS_DIR, "q19_top5_students.png"))
plt.close()

# =====================
# Visual 5: Performance Category
# =====================

performance_count.plot(kind="bar", color="green")
plt.title("City-wise Performance Category")
plt.xlabel("Performance Category")
plt.ylabel("Number of Cities")
plt.tight_layout()
plt.savefig(os.path.join(VISUALS_DIR, "q20_performance_category.png"))
plt.close()

# =====================
# Visual 6: Marks Histogram with Mean Line
# =====================

mean_marks = df["Marks"].mean()

df["Marks"].plot(kind="hist", color="yellow")
plt.axvline(mean_marks, color="red", linewidth=2, label="Mean")
plt.title("Marks Distribution with Mean Line")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(VISUALS_DIR, "q21_marks_histogram_mean.png"))
plt.close()

# =====================
# Visual 7: Student Count vs Average Marks
# =====================

count = df.groupby("City").size()
avg = df.groupby("City")["Marks"].mean()

combined = pd.DataFrame({
    "Student_Count": count,
    "Average_Marks": avg
})

combined.plot(kind="bar")
plt.title("City-wise Student Count vs Average Marks")
plt.xlabel("City")
plt.ylabel("Value")
plt.tight_layout()
plt.savefig(os.path.join(VISUALS_DIR, "q22_count_vs_average_marks.png"))
plt.close()

# =====================
# Visual 8: Young vs Old Students
# =====================

age_group_avg.plot(kind="bar", color=["green", "orange"])
plt.title("Young vs Old Students Performance")
plt.xlabel("Age Group")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.savefig(os.path.join(VISUALS_DIR, "q23_young_vs_old.png"))
plt.close()

# =====================
# Visual 9: Marks Range Distribution
# =====================

marks_range_count.plot(kind="bar", color="purple")
plt.title("Marks Distribution by Range")
plt.xlabel("Marks Range")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig(os.path.join(VISUALS_DIR, "q24_marks_range_distribution.png"))
plt.close()

# =====================
# Insights
# =====================

best_city = avg_marks.idxmax()
weak_city = avg_marks.idxmin()
highest_topper = topper.iloc[0]["Name"]
highest_marks = topper.iloc[0]["Marks"]

insights = f"""
STUDENT PERFORMANCE ANALYSIS - INSIGHTS

1. Overall Topper:
   - Student {highest_topper} scored the highest marks with {highest_marks} marks.

2. City-wise Performance:
   - {best_city} has the highest average marks.
   - {weak_city} has the lowest average marks.
   - This shows that performance differs clearly across cities.

3. High Performers:
   - Delhi and Chennai show strong high-performer percentage.
   - Mumbai and Pune have lower high-performer presence.

4. Top Students:
   - The top 5 students are clearly identified using marks ranking.
   - Sorting helps compare high-performing students easily.

5. Age vs Marks:
   - The scatter plot helps check whether age affects marks.
   - In this small dataset, marks do not show a strong clear relationship with age.

6. Young vs Old:
   - Students are divided into Young and Old groups using Age.
   - Their average marks are compared to understand group-level performance.

7. Marks Distribution:
   - Histogram shows how marks are spread.
   - The mean line helps identify whether students are scoring above or below average.

8. Marks Range:
   - Marks are divided into ranges using pd.cut().
   - This helps understand which score range has the most students.

9. Final Conclusion:
   - Delhi performs strongly overall.
   - Some cities need improvement based on average marks and high-performer percentage.
   - This project covers data cleaning, filtering, groupby, aggregation, visualization, and insight writing.
"""

with open(INSIGHTS_PATH, "w", encoding="utf-8") as file:
    file.write(insights)

print("Project completed successfully.")
print("All graphs saved in visuals folder.")
print("Insights saved in insights.txt.")