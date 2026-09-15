# Matplotlib — Histograms

## What you'll learn

Histograms visualize the frequency distribution of a continuous dataset by grouping values into ranges called **bins**.

### Basic Syntax

```python
plt.hist(data, bins=10)
```

### Key Parameters

- **`bins`**: Number of equal-width bins (e.g. `bins=5`) or custom bin boundaries.
- **`edgecolor`**: Border color around bins (e.g. `edgecolor="black"`).
- **`color`**: Fill color for the bars.
- **`alpha`**: Opacity (`0.0` to `1.0`), useful when overlaying two datasets.

### Histogram vs Bar Chart

- **Histogram:** Continuous numerical variable (e.g., ages, scores, heights). Bins represent intervals.
- **Bar Chart:** Categorical data (e.g., programming languages, fruits, company departments).

## Practice

The `practice.py` file contains exercises to solve independently. The `lesson.py` file contains working examples.
