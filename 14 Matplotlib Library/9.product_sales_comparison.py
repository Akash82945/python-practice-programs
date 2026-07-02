import pandas as pd
import matplotlib.pyplot as plt


# Show Category wise sale Amount first
df = pd.read_csv('Sales.csv')
print(df.columns)

df['Final Amount'] = pd.to_numeric(df['Final Amount'],errors='coerce')
category_sales = df.groupby('Category')['Final Amount'].sum()

print(category_sales)




# Plot the graph according the tasks
df = pd.read_csv('Sales.csv')

df['Final Amount'] = pd.to_numeric(df['Final Amount'], errors='coerce')
df['Final Amount'] = df['Final Amount'].fillna(0)

category_sales = df.groupby('Category')['Final Amount'].sum()

fig, ax = plt.subplots(figsize=(9,6))

bar = category_sales.plot(kind='bar', color='firebrick', edgecolor='black', label='Product Sales')

ax.bar_label(ax.containers[0], fmt='₹%.0f', padding=3, fontsize=10)

plt.title('Product Category Wise sale comparison.')
plt.xlabel('Products Category')
plt.ylabel('Sales Amount(INR)')

plt.ylim(0, category_sales.max()*1.15)

plt.grid(True, axis='y', linestyle='--', alpha=0.5)
plt.xticks(rotation=30)
plt.legend()
plt.tight_layout()
plt.show()