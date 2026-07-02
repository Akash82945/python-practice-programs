import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Sales.csv')

df['Final Amount'] = pd.to_numeric(df['Final Amount'], errors='coerce')
df['Final Amount'] = df['Final Amount'].fillna(0)

category_sales = df.groupby('Category')['Final Amount'].sum()
payment_mode = df['Payment Mode'].value_counts()
location_sales = df.groupby('Location')['Final Amount'].sum()
catogery_quantity= df.groupby('Category')['Quantity'].count()


fig, axes = plt.subplots(2,2, figsize=(14,10))

category_sales.plot(kind='bar', color='red', edgecolor='black', alpha=0.8, ax=axes[0,0])
axes[0,0].set_title('Product wise Sales')
axes[0,0].set_ylabel('Sales Amount (INR)')
# axes[0,0].set_xlabel('Product category', fontsize=10, labelpad=15)
axes[0,0].set_ylim(0, category_sales.max()*1.15)
axes[0,0].tick_params(axis='x', rotation=30)
axes[0,0].grid(True, axis='y', linestyle='--', alpha=0.5)
axes[0,0].bar_label(axes[0,0].containers[0], fmt='₹%.0f', padding=3, fontsize=10)


payment_mode.plot(kind='pie', autopct='%1.1f%%', colors=['red','orange','yellow'], startangle=90, label='Payment Mode', ax=axes[0,1], wedgeprops={'edgecolor':'black'})
axes[0,1].set_title('Payment Mode', fontweight='bold', fontsize=12)
axes[0,1].set_ylabel('Sales share by Payment mode', fontsize=12)



location_sales.plot(kind='barh', color='teal', edgecolor='black', ax=axes[1,0])
axes[1,0].set_title("Location wise Sales",fontsize=12, fontweight='bold')
axes[1,0].set_ylabel("Sales Amount",fontsize=10)
axes[1,0].tick_params(axis='x', rotation=30)
axes[1,0].set_xlim(0, location_sales.max()*1.25)
axes[1,0].grid(True, axis='x', linestyle='--', alpha=0.7)
axes[1,0].bar_label(axes[1,0].containers[0], fmt='₹%.0f', padding=3, fontsize=10)



catogery_quantity.plot(kind='line', color='red', ax=axes[1,1])
axes[1,1].set_title("Categoey wise Order", fontsize=12, fontweight='bold')
axes[1,1].set_ylabel('Categoey',fontsize=10)
axes[1,1].tick_params(axis='x', rotation=30)
axes[1,1].grid(True, linestyle='--', alpha=0.7)


for i,v in enumerate(catogery_quantity):
    axes[1,1].text(i,v + 0.2, str(v), ha='center', color='darkred')

plt.tight_layout(rect=[0,0,1,0.95])
plt.show()