import matplotlib.pyplot as plt

# Matplotlib Lesson 3: Bar Charts

# Categories
products = ["Python", "Java", "C++", "JavaScript"]

# Values for each category
students = [45, 30, 25, 40]

# Create a bar chart
plt.bar(products, students)

plt.xlabel("Programming Language")
plt.ylabel("Number of Students")
plt.title("Programming Language Preferences")

plt.show()

# Another example: monthly sales
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 150, 100, 180, 160]

plt.bar(months, sales)

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales")

plt.show()
