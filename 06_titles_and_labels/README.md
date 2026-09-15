# Matplotlib — Titles and Labels

## What you'll learn

Labels and titles communicate the meaning and context of your visualization.

### Enhancing Titles

```python
plt.title(
    "Title Text",
    fontsize=16,
    fontweight="bold",
    color="#2c3e50",
    pad=15
)
```

- **`fontsize`**: Size in points (e.g. `14`, `16`).
- **`fontweight`**: Font weight (`'bold'`, `'semibold'`, `'normal'`).
- **`pad`**: Spacing between the title and the chart.

### Enhancing Axis Labels

```python
plt.xlabel("X Axis Name", fontsize=12)
plt.ylabel("Y Axis Name", fontsize=12)
```

### Controlling Axis Limits

- `plt.xlim(min, max)`: Sets lower and upper bounds of X-axis.
- `plt.ylim(min, max)`: Sets lower and upper bounds of Y-axis.

## Practice

The `practice.py` file contains exercises to solve independently. The `lesson.py` file contains working examples.
