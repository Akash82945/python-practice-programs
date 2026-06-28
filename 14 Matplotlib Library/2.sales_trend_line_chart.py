import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Sales.csv')
print(df.head())



df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df = df.sort_values('OrderDate')

sales = df['Final Amount']
date = df['OrderDate']

plt.plot(date, sales, color= 'red', label= 'Sales trends', marker= 'o', markersize= 4)
plt.title('Sales trend line chart')
plt.xlabel("Sales Date")
plt.ylabel('Sales Amount')
plt.xticks(rotation=45, ha='right')
plt.grid(True, linestyle= ':', alpha= 0.6)
plt.legend()
plt.tight_layout()
plt.show()





df['Months'] = pd.to_datetime(df['OrderDate']).dt.strftime('%B')
monthly_sales = df.groupby('Months')['Final Amount'].sum().reindex(['January', 'February','March'])
plt.bar(monthly_sales.index, monthly_sales.values, color=['orange','red','yellow'], label="Monthly sales")
plt.title('Monthly sales')
plt.xlabel('Months')
plt.ylabel('Sales Amount')
plt.legend()
plt.xticks(rotation= 45)
plt.grid(True ,linestyle=':', alpha=0.74)
plt.tight_layout()
plt.show()