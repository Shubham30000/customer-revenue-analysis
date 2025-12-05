import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic monthly revenue data for different customer segments
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Create data for three customer segments with realistic seasonal patterns
data = []
for month_idx, month in enumerate(months):
    # Premium segment - higher baseline, strong holiday season
    premium_base = 85000 + (month_idx * 2000)
    if month_idx >= 10:  # Nov-Dec boost
        premium_base += 25000
    premium = premium_base + np.random.normal(0, 3000)
    
    # Standard segment - moderate baseline, moderate seasonality
    standard_base = 45000 + (month_idx * 1000)
    if month_idx >= 10:  # Nov-Dec boost
        standard_base += 12000
    standard = standard_base + np.random.normal(0, 2000)
    
    # Budget segment - lower baseline, less seasonal variation
    budget_base = 22000 + (month_idx * 500)
    if month_idx >= 10:  # Nov-Dec boost
        budget_base += 5000
    budget = budget_base + np.random.normal(0, 1500)
    
    data.append({'Month': month, 'Revenue': premium, 'Segment': 'Premium'})
    data.append({'Month': month, 'Revenue': standard, 'Segment': 'Standard'})
    data.append({'Month': month, 'Revenue': budget, 'Segment': 'Budget'})

# Create DataFrame
df = pd.DataFrame(data)

# Set Seaborn style for professional appearance
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=0.9)

# Create figure with specified size
plt.figure(figsize=(8, 8))

# Create lineplot with professional styling
sns.lineplot(data=df, x='Month', y='Revenue', hue='Segment', 
             palette=['#2E86AB', '#A23B72', '#F18F01'],
             linewidth=2.5, marker='o', markersize=8)

# Customize the plot
plt.title('Monthly Revenue Trends by Customer Segment', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Month', fontsize=13, fontweight='bold')
plt.ylabel('Revenue ($)', fontsize=13, fontweight='bold')

# Format y-axis to show values in thousands
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Customize legend
plt.legend(title='Customer Segment', title_fontsize=11, 
           fontsize=10, loc='upper left', frameon=True)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save the chart as PNG with exactly 512x512 pixels
plt.savefig('chart.png', dpi=64, bbox_inches='tight')

print("Chart generated successfully: chart.png")
print(f"Chart dimensions: 512x512 pixels")
