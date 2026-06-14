import pandas as pd
import numpy as np

df = pd.read_csv('Sales.csv')


# Create DATAFRAME
# cust = df['CustomerID']
# qunt = df['Quantity']
# print(cust[1:5])
# print(qunt[1:5])



# Print head() of dataframe
# df_head = df.head()
# print(f"Top 5 row of DataFrame: \n{df_head}")



# Print tail() of dataframe
# df_tail = df.tail()
# print(f"Bottom 5 row of DataFrame : \n{df_tail}")




# Info of dataframe
# print(f"Information of DataFrame :")
# df_info = df.info()




# Describe of dataframe
# df_describe = df.describe()
# print(f"Describe of DataFrame : \n{df_describe}")




# Shape of dataframe
# df_shape = df.shape
# print(f"Shape of DataFrame : \n{df_shape}")





# Column Access
# df_info = df.info()
# print(df_info)
# oredr_id = df['OrderID']
# category = df['Category']
# print(oredr_id[1:5])
# print(category[1:5])





# Filter Data
# quantity = df[df['Quantity'] > 2]
# print(quantity)




# Add column
# random_profit = np.random.uniform(0.05, 0.25, size = len(df))
# df["Profit"] = (df['Amount_INR'] * random_profit).round(2)
# print(df.head())




# Groupby Dataframe
# group_amount = df.groupby('Category')['Amount_INR'].mean().round(2)
# print(group_amount)




# Print sum or mean both
# category_summary = df.groupby('Category')['Amount_INR'].agg(['sum', 'mean']).round(2)
# print(category_summary)




# Find Highest Spending Money Customer
rich_customer = df.groupby('CustomerID')['Amount_INR'].sum().sort_values(ascending=False)
print(rich_customer)