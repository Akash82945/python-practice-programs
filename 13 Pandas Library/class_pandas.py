import pandas as pd

df = pd.read_csv('Sales.csv')


# Create DATAFRAME
# cust = df['CustomerID']
# qunt = df['Quantity']
# print(cust[1:5])
# print(qunt[1:5])



# Print head() of dataframe
df_head = df.head()
print(f"Top 5 row of DataFrame: \n{df_head}")