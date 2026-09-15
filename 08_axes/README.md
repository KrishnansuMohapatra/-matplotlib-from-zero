# Matplotlib — Axes & The Object-Oriented Interface

## What you'll learn

While `plt.plot()` is quick for simple charts, the **Object-Oriented (OO) interface** (`fig, ax = plt.subplots()`) provides explicit control over figures and axes.

### Figure vs Axes

- **`Figure` (`fig`)**: The entire canvas window.
- **`Axes` (`ax`)**: The individual chart containing lines, bars, labels, and ticks.

```python
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, y)
ax.set_title("Title")
ax.set_xlabel("X-Axis")
ax.set_ylabel("Y-Axis")
```

### Pyplot vs OO Method Mapping

| Pyplot (`plt`) | OO Interface (`ax`) |
|---|---|
| `plt.title()` | `ax.set_title()` |
| `plt.xlabel()` | `ax.set_xlabel()` |
| `plt.ylabel()` | `ax.set_ylabel()` |
| `plt.xlim()` | `ax.set_xlim()` |
| `plt.ylim()` | `ax.set_ylim()` |
| `plt.grid()` | `ax.grid()` |

## Practice

The `practice.py` file contains exercises to solve independently. The `lesson.py` file contains working examples.
