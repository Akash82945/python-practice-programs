import pandas as pd

df = pd.read_csv('Sales.csv')

# Analyze Sales Dataset

# print(df.head())

# print('\n\nInfo of sales dataset:')
# print(df.info())


# print(f"\nShape of sales dataset : {df.shape}")



# total_amount = df['Amount_INR'].sum()
# total_quantity = df['Quantity'].sum()

# print(f"Total Amount INR : {total_amount}")
# print(f"Total Quantity : {total_quantity}")


# product_performance = df.groupby('Category')['Quantity'].sum().sort_values(ascending=False)
# print(f"\nProdect Performance : \n{product_performance}")



# customer_product = df.groupby('Category')['CustomerID'].count()
# print(f"Customer Category : {customer_product}")

# if 'Fitness' in customer_product:
    print(f"\nNO of customer who buy Fitness Kit : {customer_product['Fitness']}")
    
# Find unique customer
unique_customer = df.groupby('Category')['CustomerID'].unique()
print(f"Unique Customer who buy fitness kit : {unique_customer.get('Fitness',0)}")
