import numpy as np


# Array inspection
# arr = np.array([[1,2,4],[4,5,6]])
# print(f"Array {arr.ndim}D : \n{arr}")
# print(f"Dimension of Array : {arr.ndim}")
# print(f"Shape of array : {arr.shape}")
# print(f"Data type of array : {arr.dtype}")



# Array vectorization
# Normal list method (slow)
# prices = [10,20,30]
# new_prices = [p + 2 for p in prices]
# print(f"Prices : {prices}")
# print(f"New Prices after add $2 : {new_prices}")

# NumPy method (fast)
# prices_arr = np.array([10,20,30])
# new_prices_arr = prices_arr + 2
# print(f"Price : {prices_arr}")
# print(f"New Prices after add 2$ : {new_prices_arr}")




# Array indexing and slicing
# 1D array
# price = np.arange(1,1000)
# slice_data = price[::100]
# print(slice_data)

# 2D array
# price = np.arange(1,10)
# matrix = price.reshape(3,3)
# print("\nMartix :\n",matrix)
# print('\nIndex number : ',matrix[1,2])
# print('\nSlicing :\n',matrix[:, :2])
# print('\nSub matrix : \n',matrix[1:3,0:2])




# Basic Aggregation 
price = np.random.randint(1, 100, size=15)
min = np.min(price)
max = np.max(price)
mean = np.mean(price)
median = np.median(price)


print(f'''
Price : {price}
Min price : {min}
Max price : {max}
Mean : {mean:.2f}
Median : {median}
''')