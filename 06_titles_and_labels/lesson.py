import matplotlib.pyplot as plt

# Matplotlib Lesson 6: Titles and Labels

# Customizing titles, labels, and limits makes charts clear and easy to understand.

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [12000, 15000, 14000, 18500, 21000, 24000]

plt.plot(months, revenue, marker="o", color="#1f77b4", linewidth=2.5, markersize=8)

# 1. Customizing Title: fontsize, fontweight, color, and padding
plt.title(
    "H1 2026 Monthly Revenue Growth",
    fontsize=16,
    fontweight="bold",
    color="#2c3e50",
    pad=15
)

# 2. Customizing Axis Labels
plt.xlabel("Fiscal Month", fontsize=12, fontweight="semibold", color="#34495e")
plt.ylabel("Revenue ($ USD)", fontsize=12, fontweight="semibold", color="#34495e")

# 3. Explicit Axis Limits (ylim)
plt.ylim(10000, 26000)

# 4. Adding a Grid
plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()
