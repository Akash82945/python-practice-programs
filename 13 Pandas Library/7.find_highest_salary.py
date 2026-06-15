import pandas as pd
import numpy as np

df = pd.read_csv('Sales.csv')
# print(df.head())

# Find Highest Salay of Customer

# highest_salary = df['Salary'].sort_values(ascending=False)
# print(f"Highest Salary Customer : \n{highest_salary[:5]}")




# Groupby Payment Mode
# payment_category = df.groupby('Payment Mode')['Final Amount'].sum()
# print(payment_category)



# # Group by location
# location_analysis = df.groupby('Location').agg({
#     'OrderID' : 'count',
#     'Final Amount' : 'sum'
# }).sort_values(by='Final Amount', ascending=False)
# print(location_analysis)




# Pivot Table
pivot_tabel = df.pivot_table(
    values = 'Final Amount',
    index= 'Location',
    columns= 'Category',
    aggfunc= 'sum',
    fill_value= 0
)

pivot_tabel['Total'] = pivot_tabel.sum(axis=1)
pivot_tabel = pivot_tabel.sort_values(by= 'Total', ascending=False)
print(pivot_tabel)