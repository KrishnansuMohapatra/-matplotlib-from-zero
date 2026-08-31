import numpy as np
import matplotlib.pyplot as plt

# Lesson 2 practice

days = np.array([1, 2, 3, 4, 5])
sales = np.array([100, 150, 120, 200, 180])

# Create a line chart
plt.plot(days, sales, marker="o")

# Add labels and title
plt.xlabel("Day")
plt.ylabel("Sales")
plt.title("Daily Sales")

# Second sales data
sales_2 = np.array([80, 130, 160, 170, 210])

# Plot the second line
plt.plot(days, sales_2, marker="x")

plt.show()
