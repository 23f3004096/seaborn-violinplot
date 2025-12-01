# Customer Support Efficiency Analysis - Violin Plot
# Email: 23f3004096@ds.study.iitm.ac.in

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate realistic synthetic data for support response times
# Simulating 300 support tickets across three channels

# Email support: Generally slower, higher variance (8-24 hours typical)
email_times = np.random.gamma(shape=3, scale=4, size=100)

# Live Chat: Faster, more consistent (1-6 hours typical)
chat_times = np.random.gamma(shape=2, scale=1.5, size=100)

# Phone Support: Fastest, very consistent (0.5-4 hours typical)
phone_times = np.random.gamma(shape=1.5, scale=1, size=100)

# Create a pandas DataFrame
data = pd.DataFrame({
    'Response Time (hours)': np.concatenate([email_times, chat_times, phone_times]),
    'Support Channel': ['Email'] * 100 + ['Live Chat'] * 100 + ['Phone'] * 100
})

# Set Seaborn style for professional appearance
sns.set_style("whitegrid")

# Set context for presentation-ready text sizes
sns.set_context("notebook", font_scale=1.2)

# Create figure with specific size for exactly 512x512 output
# Remove bbox_inches='tight' to maintain exact dimensions
fig = plt.figure(figsize=(512/100, 512/100), dpi=100)

# Create the violin plot
sns.violinplot(
    data=data,
    x='Support Channel',
    y='Response Time (hours)',
    palette='Set2',  # Professional color palette
    inner='quartile',  # Show quartiles inside violin
    linewidth=1.5
)

# Customize the plot
plt.title('Customer Support Response Time Distribution', 
          fontsize=14, 
          fontweight='bold', 
          pad=15)

plt.xlabel('Support Channel', fontsize=11, fontweight='bold')
plt.ylabel('Response Time (hours)', fontsize=11, fontweight='bold')

# Add a grid for better readability
plt.grid(axis='y', alpha=0.3, linestyle='--')

# Adjust layout
plt.tight_layout()

# Save the chart as PNG with EXACTLY 512x512 pixels
# Key: Remove bbox_inches='tight' to keep exact dimensions
plt.savefig('chart.png', dpi=100)

plt.close()

print("Chart generated successfully: chart.png (512x512 pixels)")
print("Violin plot shows response time distributions across support channels")
