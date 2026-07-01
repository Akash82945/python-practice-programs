import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Sales.csv')
# print(df.head())
# print(df.columns)

df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df = df.sort_values('OrderDate')

monthly_df = df.groupby(df['OrderDate'].dt.to_period('M'))['Salary'].sum().reset_index()

month = monthly_df['OrderDate'].astype(str)
salary = monthly_df['Salary']

plt.plot(month, salary, label='Monthly Income.', marker='o', markersize=4)
plt.title('Monthly Income Chart.')
plt.xlabel('Months Date.')
plt.ylabel('Income INR.')
# plt.grid(True)
plt.tight_layout()
plt.xticks(rotation=30)
plt.show()