import pandas as pd
import matplotlib.pyplot as plt
import os

# ==================================================
# PATHS
# ==================================================

DATA_PATH = r"C:\Users\MAINAK\Desktop\SQl\Pandas\projects\student_analysis\data\data.csv"
CLEANED_PATH = r"C:\Users\MAINAK\Desktop\SQl\Pandas\projects\student_analysis\data\cleaned_students.csv"
VISUALS_DIR = r"C:\Users\MAINAK\Desktop\SQl\Pandas\projects\student_analysis\visuals"
INSIGHTS_PATH = r"C:\Users\MAINAK\Desktop\SQl\Pandas\projects\student_analysis\insights.txt"

os.makedirs(VISUALS_DIR, exist_ok=True)

# ==================================================
# CREATE UPGRADED DATASET
# ==================================================

df = pd.DataFrame({
    "Name": [
        "Aarav","Priya","Rohan","Sneha","Karan","Meera","Aman","Isha","Rahul","Ananya",
        "Vikram","Nisha","Dev","Pooja","Arjun","Kavya","Mohit","Riya","Sahil","Tanya",
        "Yash","Neha","Harsh","Simran","Aditya","Mansi","Rakesh","Divya","Nitin","Shreya"
    ],
    "City": [
        "Delhi","Mumbai","Pune","Delhi","Chennai","Mumbai","Delhi","Pune","Jaipur","Delhi",
        "Mumbai","Chennai","Jaipur","Pune","Delhi","Mumbai","Chennai","Jaipur","Pune","Delhi",
        "Mumbai","Jaipur","Chennai","Pune","Delhi","Mumbai","Jaipur","Chennai","Pune","Delhi"
    ],
    "Subject": [
        "Python","SQL","Python","Pandas","Python","SQL","Pandas","Python","SQL","Pandas",
        "Python","Pandas","SQL","Python","SQL","Pandas","Python","SQL","Pandas","Python",
        "SQL","Pandas","Python","SQL","Pandas","Python","SQL","Pandas","Python","SQL"
    ],
    "Gender": [
        "Male","Female","Male","Female","Male","Female","Male","Female","Male","Female",
        "Male","Female","Male","Female","Male","Female","Male","Female","Male","Female",
        "Male","Female","Male","Female","Male","Female","Male","Female","Male","Female"
    ],
    "Age": [21,22,23,21,22,23,24,21,22,20,23,22,21,24,22,23,21,22,24,20,23,21,22,24,21,22,23,20,24,21],
    "Marks": [88,72,91,65,78,58,84,69,55,93,74,81,49,67,86,79,92,61,73,95,57,82,76,64,89,71,52,85,68,90],
    "Attendance": [92,85,96,78,88,70,91,82,68,97,84,89,60,75,93,87,95,73,80,98,66,90,83,72,94,86,64,92,79,96],
    "Study_Hours": [5,3,6,2,4,2,5,3,1,7,4,5,1,3,6,4,7,2,3,8,2,5,4,3,6,4,1,6,3,7]
})

df.to_csv(DATA_PATH, index=False)

# ==================================================
# LOAD DATASET
# ==================================================

df = pd.read_csv(DATA_PATH)

# ==================================================
# BASIC INFO
# ==================================================

print("\n========== FIRST 5 ROWS ==========\n")
print(df.head())

print("\n========== DATASET SHAPE ==========\n")
print(df.shape)

print("\n========== COLUMN NAMES ==========\n")
print(df.columns)

print("\n========== DATA TYPES ==========\n")
print(df.dtypes)

print("\n========== MISSING VALUES ==========\n")
print(df.isnull().sum())

# ==================================================
# DATA CLEANING
# ==================================================

df = df.dropna()

df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")
df["Attendance"] = pd.to_numeric(df["Attendance"], errors="coerce")
df["Study_Hours"] = pd.to_numeric(df["Study_Hours"], errors="coerce")

df = df.dropna()

# ==================================================
# FEATURE ENGINEERING
# ==================================================

def performance_category(x):
    if x >= 85:
        return "Excellent"
    elif x >= 70:
        return "Good"
    elif x >= 50:
        return "Average"
    else:
        return "Poor"

df["Performance"] = df["Marks"].apply(performance_category)

df["Age_Group"] = df["Age"].apply(
    lambda x: "Young" if x < 23 else "Old"
)

bins = [0, 40, 60, 80, 100]
labels = ["0-40", "40-60", "60-80", "80-100"]

df["Marks_Range"] = pd.cut(
    df["Marks"],
    bins=bins,
    labels=labels,
    include_lowest=True
)

df.to_csv(CLEANED_PATH, index=False)

print("\n========== CLEANED DATA ==========\n")
print(df.head())

# ==================================================
# ANALYSIS
# ==================================================

topper = df.sort_values(by="Marks", ascending=False).head(1)
top10 = df.sort_values(by="Marks", ascending=False).head(10)

city_avg_marks = df.groupby("City")["Marks"].mean().sort_values(ascending=False)
city_total_marks = df.groupby("City")["Marks"].sum()
city_student_count = df.groupby("City")["Name"].count()

subject_avg_marks = df.groupby("Subject")["Marks"].mean().sort_values(ascending=False)
subject_total_students = df.groupby("Subject")["Name"].count()

gender_avg_marks = df.groupby("Gender")["Marks"].mean()
age_group_avg_marks = df.groupby("Age_Group")["Marks"].mean()

performance_count = df["Performance"].value_counts()
marks_range_count = df["Marks_Range"].value_counts().sort_index()

attendance_avg_city = df.groupby("City")["Attendance"].mean()
study_hours_avg_subject = df.groupby("Subject")["Study_Hours"].mean()

high_performers = df[df["Marks"] >= 85]
weak_students = df[df["Marks"] < 60]

subject_city_pivot = pd.pivot_table(
    df,
    values="Marks",
    index="City",
    columns="Subject",
    aggfunc="mean"
)

correlation = df[["Marks", "Attendance", "Study_Hours"]].corr()

print("\n========== TOPPER ==========\n")
print(topper)

print("\n========== TOP 10 STUDENTS ==========\n")
print(top10)

print("\n========== CITY AVERAGE MARKS ==========\n")
print(city_avg_marks)

print("\n========== SUBJECT AVERAGE MARKS ==========\n")
print(subject_avg_marks)

print("\n========== GENDER AVERAGE MARKS ==========\n")
print(gender_avg_marks)

print("\n========== PERFORMANCE COUNT ==========\n")
print(performance_count)

print("\n========== CORRELATION ==========\n")
print(correlation)

# ==================================================
# VISUALIZATIONS
# ==================================================

# Graph 1: City-wise Average Marks
city_avg_marks.plot(kind="bar", figsize=(9, 5))
plt.title("City-wise Average Marks")
plt.xlabel("City")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.savefig(os.path.join(VISUALS_DIR, "01_city_avg_marks.png"))
plt.show()
plt.close()

# Graph 2: City-wise Total Marks
city_total_marks.plot(kind="bar", figsize=(9, 5))
plt.title("City-wise Total Marks")
plt.xlabel("City")
plt.ylabel("Total Marks")
plt.tight_layout()
plt.savefig(os.path.join(VISUALS_DIR, "02_city_total_marks.png"))
plt.show()
plt.close()

# Graph 3: City-wise Student Count
city_student_count.plot(kind="bar", figsize=(9, 5))
plt.title("City-wise Student Count")
plt.xlabel("City")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig(os.path.join(VISUALS_DIR, "03_city_student_count.png"))
plt.show()
plt.close()

# Graph 4: Subject-wise Average Marks
subject_avg_marks.plot(kind="bar", figsize=(9, 5))
plt.title("Subject-wise Average Marks")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.savefig(os.path.join(VISUALS_DIR, "04_subject_avg_marks.png"))
plt.show()
plt.close()

# Graph 5: Subject-wise Student Count
subject_total_students.plot(kind="bar", figsize=(9, 5))
plt.title("Subject-wise Student Count")
plt.xlabel("Subject")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig(os.path.join(VISUALS_DIR, "05_subject_student_count.png"))
plt.show()
plt.close()

# Graph 6: Gender-wise Average Marks
gender_avg_marks.plot(kind="bar", figsize=(8, 5))
plt.title("Gender-wise Average Marks")
plt.xlabel("Gender")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.savefig(os.path.join(VISUALS_DIR, "06_gender_avg_marks.png"))
plt.show()
plt.close()

# Graph 7: Top 10 Students
top10.plot(x="Name", y="Marks", kind="bar", figsize=(10, 5))
plt.title("Top 10 Students by Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig(os.path.join(VISUALS_DIR, "07_top10_students.png"))
plt.show()
plt.close()

# Graph 8: Performance Category Count
performance_count.plot(kind="bar", figsize=(8, 5))
plt.title("Performance Category Distribution")
plt.xlabel("Performance Category")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig(os.path.join(VISUALS_DIR, "08_performance_category.png"))
plt.show()
plt.close()

# Graph 9: Marks Range Distribution
marks_range_count.plot(kind="bar", figsize=(8, 5))
plt.title("Marks Range Distribution")
plt.xlabel("Marks Range")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig(os.path.join(VISUALS_DIR, "09_marks_range.png"))
plt.show()
plt.close()

# Graph 10: Marks Histogram with Mean Line
mean_marks = df["Marks"].mean()

df["Marks"].plot(kind="hist", bins=10, figsize=(8, 5))
plt.axvline(mean_marks, color="red", linewidth=2, label="Mean")
plt.title("Marks Distribution with Mean Line")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(VISUALS_DIR, "10_marks_histogram_mean.png"))
plt.show()
plt.close()

# Graph 11: Attendance vs Marks
plt.figure(figsize=(8, 5))
plt.scatter(df["Attendance"], df["Marks"])
plt.title("Attendance vs Marks")
plt.xlabel("Attendance (%)")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig(os.path.join(VISUALS_DIR, "11_attendance_vs_marks.png"))
plt.show()
plt.close()

# Graph 12: Study Hours vs Marks
plt.figure(figsize=(8, 5))
plt.scatter(df["Study_Hours"], df["Marks"])
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig(os.path.join(VISUALS_DIR, "12_study_hours_vs_marks.png"))
plt.show()
plt.close()

# Graph 13: Age Group Average Marks
age_group_avg_marks.plot(kind="bar", figsize=(8, 5))
plt.title("Age Group-wise Average Marks")
plt.xlabel("Age Group")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.savefig(os.path.join(VISUALS_DIR, "13_age_group_avg_marks.png"))
plt.show()
plt.close()

# Graph 14: Average Attendance by City
attendance_avg_city.plot(kind="bar", figsize=(9, 5))
plt.title("City-wise Average Attendance")
plt.xlabel("City")
plt.ylabel("Average Attendance")
plt.tight_layout()
plt.savefig(os.path.join(VISUALS_DIR, "14_city_avg_attendance.png"))
plt.show()
plt.close()

# Graph 15: Subject City Pivot
subject_city_pivot.plot(kind="bar", figsize=(11, 6))
plt.title("City vs Subject Average Marks")
plt.xlabel("City")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.savefig(os.path.join(VISUALS_DIR, "15_city_subject_pivot.png"))
plt.show()
plt.close()

# Graph 16: Correlation Matrix
plt.figure(figsize=(7, 5))
plt.imshow(correlation)
plt.colorbar()
plt.xticks(range(len(correlation.columns)), correlation.columns)
plt.yticks(range(len(correlation.columns)), correlation.columns)
plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig(os.path.join(VISUALS_DIR, "16_correlation_matrix.png"))
plt.show()
plt.close()

# ==================================================
# INSIGHTS
# ==================================================

best_city = city_avg_marks.idxmax()
weak_city = city_avg_marks.idxmin()

best_subject = subject_avg_marks.idxmax()
weak_subject = subject_avg_marks.idxmin()

highest_topper = topper.iloc[0]["Name"]
highest_marks = topper.iloc[0]["Marks"]

insights = f"""
STUDENT PERFORMANCE ANALYSIS - INSIGHTS

1. Dataset Overview:
   - The upgraded dataset contains 30 students.
   - It includes Name, City, Subject, Gender, Age, Marks, Attendance, and Study_Hours.
   - This makes the project more realistic than the previous small dataset.

2. Overall Topper:
   - Student {highest_topper} scored the highest marks with {highest_marks} marks.

3. City-wise Performance:
   - {best_city} has the highest average marks.
   - {weak_city} has the lowest average marks.
   - City-wise analysis helps compare regional performance.

4. Subject-wise Performance:
   - {best_subject} has the highest average marks.
   - {weak_subject} has the lowest average marks.
   - Subject-wise analysis helps identify stronger and weaker academic areas.

5. Gender-wise Performance:
   - Gender-wise average marks help compare performance patterns between groups.
   - This analysis is useful for balanced academic reporting.

6. Attendance vs Marks:
   - Scatter plot helps check whether attendance is related to marks.
   - Higher attendance generally supports better academic performance.

7. Study Hours vs Marks:
   - Study hours are compared with marks to understand learning effort.
   - Students with more study hours tend to show better performance.

8. Performance Categories:
   - Students are divided into Excellent, Good, Average, and Poor categories.
   - This helps understand overall performance distribution.

9. Marks Range:
   - Marks are divided into score ranges using pd.cut().
   - This helps understand which marks range contains the most students.

10. Final Conclusion:
   - This upgraded project covers data creation, CSV export, cleaning, feature engineering, groupby analysis, pivot tables, correlation, visualization, and insight writing.
   - It is now a stronger beginner-to-intermediate EDA project using Pandas and Matplotlib.
"""

with open(INSIGHTS_PATH, "w", encoding="utf-8") as file:
    file.write(insights)

print("\n========== PROJECT COMPLETED ==========")
print("Upgraded dataset saved successfully.")
print("Cleaned dataset saved successfully.")
print("16 graphs saved in visuals folder.")
print("Insights saved successfully.")