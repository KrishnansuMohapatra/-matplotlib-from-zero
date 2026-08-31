# 02 — Line Charts

## Notes

A line chart is useful for showing how values change, especially across an ordered sequence such as days or months.

### What I learned

- Use `plt.plot()` to create a line chart.
- Give Matplotlib X and Y data explicitly.
- Add X-axis and Y-axis labels.
- Add a chart title.
- Add markers to data points.
- Plot more than one line on the same chart.

### Basic example

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [100, 150, 120, 200, 180]

plt.plot(x, y)
plt.show()
```

### Labels and title

```python
plt.xlabel("Day")
plt.ylabel("Sales")
plt.title("Daily Sales")
```

### Markers

```python
plt.plot(x, y, marker="o")
```

### Multiple lines

Call `plt.plot()` again with another set of Y values to compare two datasets.

## Practice

The `practice.py` file contains the problems I solved for this lesson.

## Key idea

**Data → X/Y points → line chart → visual trend**
