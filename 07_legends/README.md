# Matplotlib — Legends

## What you'll learn

Legends clarify multiple visual series on the same plot by associating lines or bars with descriptive labels.

### Core Steps

1. Attach a `label="..."` argument to each plotting call (`plt.plot()`, `plt.scatter()`, `plt.bar()`).
2. Call `plt.legend()` to render the legend box.

```python
plt.plot(x, y1, label="Product A")
plt.plot(x, y2, label="Product B")
plt.legend()
```

### Legend Placement (`loc`)

- `'best'` (default, finds location with least overlap)
- `'upper right'`, `'upper left'`
- `'lower right'`, `'lower left'`

## Practice

The `practice.py` file contains exercises to solve independently. The `lesson.py` file contains working examples.
