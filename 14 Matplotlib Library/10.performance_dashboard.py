import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Sales.csv')

df['Final Amount'] = pd.to_numeric(df['Final Amount'], errors='coerce')
df['Final Amount'] = df['Final Amount'].fillna(0)

category_sales = df.groupby('Category')['Final Amount'].sum()


payment_mode = df['Payment Mode']

location_sales = df.groupby('Location')['Final Amount'].sum()

category = df['Category']
quantity = df['Quantity'].count()



plt, axes = plt.subplots(2,2, figsize=(12,10))

