# Matplotlib — Bar Charts

## What you'll learn

Bar charts are useful for comparing values across different categories.

## Basic bar chart

```python
plt.bar(categories, values)
```

The first argument contains the categories on the x-axis, and the second contains the corresponding values on the y-axis.

Example:

```python
products = ["Python", "Java", "C++", "JavaScript"]
students = [45, 30, 25, 40]

plt.bar(products, students)
```

Each category must have a corresponding value.

## Adding labels and a title

```python
plt.xlabel("Programming Language")
plt.ylabel("Number of Students")
plt.title("Programming Language Preferences")
```

## When to use a bar chart

Use bar charts when you want to compare separate categories, such as:

- Products and sales
- Programming languages and users
- Months and revenue
- Departments and employee counts

## Bar chart vs line chart

**Bar chart:** best for comparing categories.

**Line chart:** best for showing trends or changes over an ordered sequence such as time.

## Practice

The `practice.py` file contains exercises to solve independently. The `lesson.py` file contains working examples.
