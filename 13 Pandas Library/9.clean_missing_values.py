import pandas as pd
import numpy as np


# Load CSV file
df = pd.read_csv("Sales.csv")

# print(df.head())

# describe = df.info()
# print(describe)


# check null values
# null = df.isna()
# print(null)



# drop_null = df.dropna()
# print(drop_null)


# Clean missing values
# clean_null = df.dropna()
# print(clean_null)


# fill values
# fill_null = df.fillna(0)
# print(fill_null) 



# fill with mean,median or mode for machine learning
# fill_mean = 
df['Salary'].fillna(df['Salary'].median())
# print(fill_mean)
print(df)