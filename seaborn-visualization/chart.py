import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic monthly revenue data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Create realistic seasonal revenue data for three customer segments
data = []
for i, month in enumerate(months):
    # Premium segment - high revenue with strong seasonality
    premium_revenue = 80000 + (i * 2500) + np.random.normal(0, 2000)
    if i >= 10:  # Holiday boost
        premium_revenue += 20000

    # Standard segment - moderate revenue
    standard_revenue = 45000 + (i * 1200) + np.random.normal(0, 1500)
    if i >= 10:
        standard_revenue += 10000

    # Budget segment - lower revenue with less variation
    budget_revenue = 22000 + (i * 600) + np.random.normal(0, 1000)
    if i >= 10:
        budget_revenue += 4000

    data.append({'Month': month, 'Revenue': premium_revenue, 'Segment': 'Premium'})
    data.append({'Month': month, 'Revenue': standard_revenue, 'Segment': 'Standard'})
    data.append({'Month': month, 'Revenue': budget_revenue, 'Segment': 'Budget'})

# Create DataFrame
df = pd.DataFrame(data)

# Ensure months appear in correct order on x-axis
df["Month"] = pd.Categorical(df["Month"], categories=months, ordered=True)

# Apply Seaborn styling
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=1.0)

# Create figure (8 in × 64 dpi = 512 px)
plt.figure(figsize=(8, 8))

# Create Seaborn lineplot
sns.lineplot(
    data=df,
    x="Month",
    y="Revenue",
    hue="Segment",
    palette="Set2",
    linewidth=2.5,
    marker="o",
    markersize=6,
)

# Add labels and title
plt.title(
    "Monthly Revenue Trends by Customer Segment",
    fontsize=16,
    fontweight="bold",
    pad=15,
)
plt.xlabel("Month", fontsize=12, fontweight="bold")
plt.ylabel("Revenue ($)", fontsize=12, fontweight="bold")

# Rotate x-axis labels
plt.xticks(rotation=45)

# Format y-axis
ax = plt.gca()
ax.yaxis.set_major_formatter(
    plt.FuncFormatter(lambda x, p: f"${x/1000:.0f}K")
)

# Customize legend
plt.legend(title="Customer Segment", loc="upper left", fontsize=9)

# Save image
plt.tight_layout()
plt.savefig("chart.png", dpi=64)
plt.close()

print("Chart saved as chart.png")
