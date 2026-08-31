import matplotlib.pyplot as plt

# Matplotlib Lesson 2: Line Charts

days = [1, 2, 3, 4, 5]
sales = [100, 150, 120, 200, 180]

# Basic line chart.
plt.plot(days, sales)
plt.show()

# Add axis labels and a title.
plt.plot(days, sales)
plt.xlabel("Day")
plt.ylabel("Sales")
plt.title("Daily Sales")
plt.show()

# Add markers to the data points.
plt.plot(days, sales, marker="o")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.title("Daily Sales")
plt.show()

# Plot two lines for comparison.
sales_1 = [100, 150, 120, 200, 180]
sales_2 = [80, 130, 160, 170, 210]

plt.plot(days, sales_1, marker="o")
plt.plot(days, sales_2, marker="x")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.title("Sales Comparison")
plt.show()
