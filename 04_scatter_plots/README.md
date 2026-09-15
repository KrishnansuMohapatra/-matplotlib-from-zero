# Matplotlib — Scatter Plots

## What you'll learn

Scatter plots show how two continuous variables relate to each other. They are ideal for detecting correlations, patterns, clusters, and outliers.

### Basic Syntax

```python
plt.scatter(x, y)
```

### Key Parameters

- **`color` / `c`**: The color of the data points.
- **`s`**: The size of each marker.
- **`alpha`**: Transparency between `0.0` and `1.0`.
- **`marker`**: Marker symbol (`'o'`, `'s'`, `'^'`, `'x'`).
- **`edgecolors`**: Outline color around markers.

### Example

```python
plt.scatter(study_hours, exam_scores, color="coral", s=100, alpha=0.8, edgecolors="black")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.title("Study Hours vs. Exam Score")
plt.show()
```

### Scatter Plot vs Line Chart

- **Scatter Plot:** Individual unrelated observations plotted to observe correlation.
- **Line Chart:** Ordered sequence (such as time series) showing trends over time.

## Practice

The `practice.py` file contains exercises to solve independently. The `lesson.py` file contains working examples.
