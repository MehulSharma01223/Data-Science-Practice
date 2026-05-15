import matplotlib.pyplot as plt

# =========================
# DATA
# =========================

students = [
    "Aman",
    "Priya",
    "Rahul",
    "Sneha",
    "Karan"
]

marks = [85, 92, 78, 88, 95]

# =========================
# FIGURE SIZE
# =========================

plt.figure(figsize=(8,5))

# =========================
# BAR GRAPH
# =========================

plt.bar(
    students,
    marks,
    color="skyblue"
)

# =========================
# TITLE & LABELS
# =========================

plt.title("Student Marks")

plt.xlabel("Students")

plt.ylabel("Marks")

# =========================
# GRID
# =========================

plt.grid(True)

# =========================
# SAVE GRAPH
# =========================

plt.savefig("student_marks_bar.png")

# =========================
# SHOW GRAPH
# =========================

plt.show()