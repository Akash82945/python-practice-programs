import pandas as pd
import numpy as np

df = pd.read_csv('Sales.csv')
# print(df.head())

# Find Highest Salay of Customer

highest_salary = df['Salary'].sort_values(ascending=False)
print(f"Highest Salary Customer : \n{highest_salary[:5]}")


df.info()