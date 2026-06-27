import numpy as np
import pandas as pd

np.random.seed(42)
num_records = 50

# 1. Order IDs (1001 से 1050)
order_ids = np.arange(1001, 1001 + num_records)

# 2. Customers name
customer_pool = [f"Cust_{i}" for i in range(1, 11)]
customers = np.random.choice(customer_pool, size=num_records)

# 3. Product Categories 
categories_pool = ['Electronics', 'Clothing', 'Home Decor', 'Books', 'Fitness']
categories = np.random.choice(categories_pool, size=num_records, p=[0.3, 0.3, 0.15, 0.15, 0.1])

# 4. Order Amounts (₹500 - ₹25000)
amounts = np.random.randint(500, 25001, size=num_records).astype(float)

# 5. Quantity (1-5 pics)
quantities = np.random.randint(1, 6, size=num_records)

# 6. Order Dates (2026 random dates)
dates_pool = pd.date_range(start='2026-01-01', end='2026-03-31', freq='D')
order_dates = np.random.choice(dates_pool, size=num_records)

# 7. ⚠️ Add Missing Values (NaN) for Data Cleaning Practice 
# Replace 10% Data with NULL values
nan_indices = np.random.choice(num_records, size=5, replace=False)
amounts[nan_indices] = np.nan

# 8. Add payment method
payment_pool = ['Cash', 'UPI', 'Card']
payment = np.random.choice(payment_pool, size=num_records)


# 9. Add location 
location_pool = ['Amritsar', 'Delhi', 'Noida', 'Mumbai', 'Bangalore']
location = np.random.choice(location_pool, size=num_records)


raw_data = {
    'OrderID': order_ids,
    'CustomerID': customers,
    'Category': categories,
    'Amount_INR': amounts,
    'Quantity': quantities,
    'OrderDate': order_dates,
    'Payment Mode' : payment,
    'Location' : location
}

df = pd.DataFrame(raw_data)

customer_size = len(df['OrderID'])
df['Salary'] = np.random.randint(20000,50000, size=customer_size)


# Add Discount 10% or 15%
df['Discount'] = np.random.randint(15,20, size=customer_size)

# Final Amount
df['Final Amount'] = df['Amount_INR'] * (1 - df['Discount']/100).round(2)


arranged_column = [
    'OrderID',
    'CustomerID',
    'Salary',
    'OrderDate',
    'Category',
    'Quantity',
    'Amount_INR',
    'Discount',
    'Final Amount',
    'Payment Mode',
    'Location'
]

df = df[arranged_column]


# Find Amount_INR null
# null_mask = df['Amount_INR'].isnull()
# df.loc[null_mask, 'Discount'] = 0
# df.loc[null_mask, 'Final Amount'] = 0
# df.loc[null_mask, 'Payment Mode'] = 'Unknown'

df.to_csv("Sales.csv", index= False)

print("=== 50 Real-World Random Dataset for Pandas Learning ===")
print(df)




