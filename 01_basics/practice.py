import matplotlib.pyplot as plt

# Basic Matplotlib Practice

days = [1, 2, 3, 4, 5]
sales = [100, 150, 120, 200, 180]

# 1. Create a line plot
plt.plot(days, sales)

# 2. Add labels
plt.xlabel("Day")
plt.ylabel("Sales")

# 3. Add a title
plt.title("Daily Sales")

# 4. Display the plot
plt.show()
