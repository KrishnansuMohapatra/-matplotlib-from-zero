import matplotlib.pyplot as plt

# Matplotlib Lesson 5: Histograms

# Histograms show the distribution and frequency of a single continuous dataset.

# 1. Basic Histogram
scores = [45, 52, 58, 62, 65, 67, 70, 72, 73, 75, 76, 78, 80, 82, 85, 87, 88, 90, 92, 95]

plt.hist(scores)
plt.xlabel("Score")
plt.ylabel("Number of Students")
plt.title("Distribution of Exam Scores")
plt.show()

# 2. Custom Bins and Edge Colors
plt.hist(scores, bins=5, color="skyblue", edgecolor="black")
plt.xlabel("Score Range")
plt.ylabel("Frequency")
plt.title("Exam Scores (5 Bins)")
plt.show()

# 3. Comparing Two Distributions
class_a = [55, 60, 62, 70, 72, 75, 78, 80, 82, 88, 90, 95]
class_b = [40, 48, 52, 58, 62, 65, 68, 70, 74, 76, 80, 84]

plt.hist(class_a, bins=6, alpha=0.6, label="Class A", color="blue", edgecolor="black")
plt.hist(class_b, bins=6, alpha=0.6, label="Class B", color="orange", edgecolor="black")

plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.title("Score Distribution: Class A vs Class B")
plt.legend()
plt.show()
