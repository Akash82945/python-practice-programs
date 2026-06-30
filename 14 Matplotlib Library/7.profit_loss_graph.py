import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Sales.csv')

# print(df.head())


# df_clean = df.dropna(subset=['Amount_INR','Final Amount']).copy()

# grouped_data = df_clean.groupby('Category')[['Salary', 'Final Amount']].sum().reset_index()

# plt.figure(figsize=(10,6))

# x_indices = range(len(grouped_data['Category']))
# bar_width = 0.35

# plt.bar([x - bar_width/2 for x in x_indices], grouped_data['Salary'],
# width = bar_width, label= 'Sales Amount (Gross Expected)', color='skyblue')

# plt.bar([x + bar_width/2 for x in x_indices], grouped_data['Final Amount'],
#         width=bar_width, label="Final Amount (Realized Revenue)", color='salmon')

# plt.title('Performance comparison: Gross sale Vales vs Final Realized Amount')
# plt.xlabel('Product Category')
# plt.ylabel('Total Value(INR)')
# plt.legend()
# plt.grid(axis='y', linestyle='--', alpha=0.5)
# plt.xticks(x_indices, grouped_data['Category'])

# plt.tight_layout()
# plt.show()








df_clean = df.dropna(subset=['Amount_INR','Final Amount']).copy()

grouped = (
    df_clean.groupby('Category')[['Amount_INR', 'Final Amount']]
    .sum()
    .reset_index()
)
grouped['Discount Given'] = grouped['Amount_INR']-grouped['Final Amount']


fig, ax = plt.subplots(figsize=(10,6))

bars_final = ax.bar(grouped['Category'], grouped['Final Amount'],
                    label="Final Realization Amount (net Revenue)",
                    color='#4CAF50', alpha=0.9, width=0.6)

bars_discount = ax.bar(grouped['Category'], grouped['Discount Given'],
                       bottom=grouped['Final Amount'],
                       label='Discount Loss/Cut',
                       color='red', alpha=0.9, width=0.6)


ax.set_title("Category wise Revenue Breakdown (Net revenue vs Discount values)")
ax.set_xlabel('Product category')
ax.set_ylabel('Amount in INR')
ax.legend(loc='upper right')

ax.grid(axis='y', linestyle='--', alpha=0.5)
ax.set_axisbelow(True)

for i, row in grouped.iterrows():
    total_val = row['Amount_INR']
    final_val = row['Final Amount']
    
    ax.text(i, total_val + 2000, f"{int(total_val):.2f}", ha='center', va='bottom', fontweight='bold')
    ax.text(i, final_val/2, f"{int(final_val):.2f}", ha='center', va='bottom', color='white', fontweight='bold')
    
plt.tight_layout()
plt.show()