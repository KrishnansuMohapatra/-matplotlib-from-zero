import matplotlib.pyplot as plt

# Matplotlib Lesson 8: Axes and the Object-Oriented Interface

# The Object-Oriented (OO) interface (`fig, ax = plt.subplots()`) provides
# direct control over figures and axes.

# 1. Standard OO Interface
fig, ax = plt.subplots(figsize=(8, 4.5))

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
temperature = [4, 6, 12, 17, 22, 26]

ax.plot(months, temperature, color="crimson", marker="o", linewidth=2.5)

# OO methods use `set_...` syntax:
ax.set_title("Average Monthly Temperature (°C)", fontsize=14, fontweight="bold")
ax.set_xlabel("Month", fontsize=11)
ax.set_ylabel("Temperature (°C)", fontsize=11)
ax.set_ylim(0, 30)

# Customizing Ticks
ax.set_yticks([0, 5, 10, 15, 20, 25, 30])
ax.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()

# 2. Twin Axes (`ax.twinx()`): Dual Y-Axes with Different Scales
rainfall_mm = [45, 38, 55, 62, 78, 92]

fig, ax1 = plt.subplots(figsize=(8, 4.5))

# Primary Axis (Left)
color_temp = "tab:red"
ax1.set_xlabel("Month")
ax1.set_ylabel("Temperature (°C)", color=color_temp)
ax1.plot(months, temperature, color=color_temp, marker="o")
ax1.tick_params(axis="y", labelcolor=color_temp)

# Secondary Axis (Right)
ax2 = ax1.twinx()
color_rain = "tab:blue"
ax2.set_ylabel("Rainfall (mm)", color=color_rain)
ax2.bar(months, rainfall_mm, color=color_rain, alpha=0.3, width=0.4)
ax2.tick_params(axis="y", labelcolor=color_rain)

plt.title("Climate: Temperature and Rainfall", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.show()
