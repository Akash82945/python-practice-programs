# import pandas as pd
# import matplotlib.pyplot as plt


# df = pd.read_csv('Sales.csv')
# # print(df.columns)

# # df['Final Amount'] =  

# catogery = df['Category']
# # print(catogery)
# sales = df['Final Amount'].sum()

# plt.bar(catogery,sales, color='red', edgecolor='black' )
# plt.title("Product Sales Comparison")
# plt.xlabel('Product Category')
# plt.ylabel("Sales Amount(INR)")
# plt.grid(True, axis='y', linestyle='--')
# plt.xticks(rotation=35)
# plt.tight_layout()
# plt.show()






# import pandas as pd

# df = pd.read_csv('Sales.csv')
# print(df.columns)

# df['Final Amount'] = pd.to_numeric(df['Final Amount'],errors='coerce')

# category_sales = df.groupby('Category')['Final Amount'].sum()

# print(category_sales)





import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Sales.csv')

df['Final Amount'] = pd.to_numeric(df['Final Amount'], errors='coerce')
df['Final Amount'] = df['Final Amount'].fillna(0)

category_sales = df.groupby('Category')['Final Amount'].sum()

plt.figure(figsize=(10,8))

category_sales.plot(kind='bar', color='firebrick', edgecolor='black', label='Product Sales')
plt.title('Product Category Wise sale comparison.')
plt.xlabel('Products Category')
plt.ylabel('Sales Amount(INR)')
plt.grid(True, axis='y', linestyle='--')
plt.legend()
plt.show()