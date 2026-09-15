import matplotlib.pyplot as plt

# Matplotlib Lesson 4: Scatter Plots

# 1. Basic Scatter Plot
# Used to observe relationships between two continuous variables
study_hours = [1, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 7, 8]
exam_scores = [50, 55, 60, 65, 62, 70, 75, 80, 82, 88, 92, 98]

plt.scatter(study_hours, exam_scores)
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.title("Study Hours vs. Exam Score")
plt.show()

# 2. Customizing Scatter Plot (color, size, marker)
house_area = [1200, 1500, 1800, 2100, 2400, 2800, 3200, 3500]
house_price = [220, 275, 310, 390, 420, 510, 580, 640]

plt.scatter(
    house_area,
    house_price,
    color="darkgreen",
    s=100,
    alpha=0.7,
    marker="o",
    edgecolors="black"
)

plt.xlabel("Living Area (sq ft)")
plt.ylabel("Price ($1,000s)")
plt.title("House Size vs Price")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()

# 3. Comparing Two Groups on the Same Plot
math_hours = [1.5, 2, 3, 4, 5, 6]
math_scores = [55, 62, 70, 78, 85, 94]

science_hours = [1, 2.5, 3.5, 4.5, 5.5, 6.5]
science_scores = [50, 68, 72, 82, 89, 96]

plt.scatter(math_hours, math_scores, color="blue", label="Math", marker="o", s=80)
plt.scatter(science_hours, science_scores, color="orange", label="Science", marker="^", s=80)

plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.title("Study Hours vs Score by Subject")
plt.legend()
plt.show()
