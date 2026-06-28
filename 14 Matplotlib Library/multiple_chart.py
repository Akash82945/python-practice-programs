
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Sales.csv')

df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df = df.sort_values('OrderDate')

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))

# trend chart
sales = df['Final Amount']
date = df['OrderDate']
axes[0, 0].plot(date, sales, color='red', label='Sales trends', marker='o', markersize=4)
axes[0, 0].set_title('Sales Trend Line Chart')
axes[0, 0].set_xlabel("Sales Date")
axes[0, 0].set_ylabel('Sales Amount')
axes[0, 0].tick_params(axis='x', rotation=45)
axes[0, 0].grid(True, linestyle=':', alpha=0.6)
axes[0, 0].legend()


# Bar chart (monthly)
df['Months'] = df['OrderDate'].dt.strftime('%B')
monthly_sales = df.groupby('Months')['Final Amount'].sum().reindex(['January', 'February', 'March'])

axes[0, 1].bar(monthly_sales.index, monthly_sales.values, color=['orange', 'red', 'yellow'])
axes[0, 1].set_title('Monthly Sales')
axes[0, 1].set_xlabel('Months')
axes[0, 1].set_ylabel('Sales Amount')
axes[0, 1].tick_params(axis='x', rotation=45)
axes[0, 1].grid(True, linestyle=':', alpha=0.74)


# pie chart
pay_mode = df['Payment Mode'].value_counts()
axes[1, 0].pie(pay_mode.values, labels=pay_mode.index, autopct='%1.1f%%', startangle=90)
axes[1, 0].set_title("Expense Pie Chart")


# sales amount location wise
location_sales = df.groupby('Location')['Final Amount'].sum()
axes[1, 1].bar(location_sales.index, location_sales.values, color='purple')
axes[1, 1].set_title('Sales by Location')
axes[1, 1].set_xlabel('Location')
axes[1, 1].set_ylabel('Sales Amount')
axes[1, 1].tick_params(axis='x', rotation=45)




plt.tight_layout() 
plt.subplots_adjust(hspace=0.5, wspace=0.3)
plt.show()



