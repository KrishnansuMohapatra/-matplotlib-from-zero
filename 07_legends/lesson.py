import matplotlib.pyplot as plt

# Matplotlib Lesson 7: Legends

quarters = ["Q1", "Q2", "Q3", "Q4"]
product_a_sales = [120, 145, 160, 190]
product_b_sales = [100, 130, 155, 175]
product_c_sales = [80, 95, 110, 140]

# 1. Use the `label` parameter in plot calls
plt.plot(quarters, product_a_sales, marker="o", color="blue", label="Product A")
plt.plot(quarters, product_b_sales, marker="s", color="green", label="Product B")
plt.plot(quarters, product_c_sales, marker="^", color="coral", linestyle="--", label="Product C")

# 2. Add title and labels
plt.title("Quarterly Product Sales Comparison", fontsize=14, fontweight="bold")
plt.xlabel("Quarter", fontsize=11)
plt.ylabel("Revenue ($k)", fontsize=11)

# 3. Customizing the Legend:
# loc: 'upper left', 'upper right', 'lower left', 'lower right', 'best'
plt.legend(
    loc="upper left",
    fontsize=10,
    frameon=True,
    shadow=True
)

plt.grid(True, linestyle=":", alpha=0.6)
plt.tight_layout()
plt.show()
