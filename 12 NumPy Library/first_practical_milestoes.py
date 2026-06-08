import numpy as np


# 1. Array inspection
# arr = np.array([[1,2,4],[4,5,6]])
# print(f"Array {arr.ndim}D : \n{arr}")
# print(f"Dimension of Array : {arr.ndim}")
# print(f"Shape of array : {arr.shape}")
# print(f"Data type of array : {arr.dtype}")



# 2. Array vectorization
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




# 3. Array indexing and slicing
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




# 4. Basic Aggregation 
# price = np.random.randint(1, 100, size=15)
# min = np.min(price)
# max = np.max(price)
# mean = np.mean(price)
# median = np.median(price)

# print(f'''
# Price : {price}
# Min price : {min}
# Max price : {max}
# Mean : {mean:.2f}
# Median : {median}
# ''')





# Boolean Masking
# marks = np.random.randint(1,101,5)

# One condition
# passed_sub = marks[marks>60]

# Two condition AND(&) , OR(|)
# passed_sub = marks[(marks>60) & (marks<80)]
# print(f"Marks : {marks}")
# print(f"Passed subjects (60<100) : {passed_sub}")


# 2D array 
# matrix_marks = np.random.randint(1,101,(3,4))
# one condition
# passed_sub = matrix_marks[matrix_marks>60]

# two condition
# passed_sub = matrix_marks[(matrix_marks>60) & (matrix_marks<80)]
# print(f"\nMatrix Marks : \n{matrix_marks}")
# print(f"\nPassed Subject : \n{passed_sub}")





# Where method 
# matrix = np.random.randint(1,101,(3,3))
# Fill 0 where marks is less then 60
# passed_sub = np.where(matrix > 60, matrix, 0) 
# Fill pass or fail text 
# passed_sub = np.where(matrix > 60, 'Pass', 'Fail')
# print(f"Matrix : \n{matrix}")
# print(f"Passed Subject : \n{passed_sub}")





# Quick Checking [np.any() | np.all()]
# 1D array
# marks = np.random.randint(1,101,5)
# any_failed = np.any(marks < 40)
# all_passed = np.all(marks >= 40)
# print(f"Marks : {marks}")
# print(f"Any failed [YES or NO] : {any_failed}")
# print(f"All Passed [YES or NO] : {all_passed}")

# 2D array
# matrix_marks = np.random.randint(1,101,(3,3))
# any_failed = np.any(matrix_marks < 40)
# any_failed = np.any(matrix_marks < 40, axis=0)   #Check Each row
# all_passed = np.all(matrix_marks >= 40)
# all_passed = np.all(matrix_marks >= 40, axis=0)  #Check Each row
# print(f'''
# \nMatrix Marks : \n{matrix_marks}
# \nAny failed student : {any_failed}
# \nAll passed student : {all_passed}
      # ''')
      
      
      
      
      
      
# Create 1D array with containing all odd numbers form 1-15
# arr = np.arange(1,16,2)
# print(f"Odd Number is : {arr}")


# Create 2D matrix with 4row and 5columns filled entirely with the number 1.0
# matrix = np.ones((4,5))
# print(f"Matrix : \n{matrix}")


# Create 1D array of numbers from 0-11, and then reshape ist into matrix with 3row and 4columns.
# arr = np.arange(0,12)
# matrix = arr.reshape(3,4)
# print(f"1D array : {arr}")
# print(f"2D array : \n{matrix}")




# Indexing or slicing
# matrix = np.array([
#     [10, 11, 12],
#     [20, 21, 22],
#     [30, 31, 32]
# ])

# Extract the number 3,1 from the index
# spec_index = matrix[2,1]
# print('Extract no 36 : ',spec_index)

# Extract the entire last row
# last_row = matrix[2:]
# print(f"Last Row : {last_row}")

# Extract the sub-grid [[20,21], [30,31]] (the bottom left 2X2 grid)
# left_grid = matrix[0:3,0:2]
# print(f"Left 2X2 bottom grid : \{left_grid}")





# Data manipulation
data = np.array([
    [10, 20, 30],
    [5,  15, 25],
    [2,  4,  6]
])

# Find max value in entire matrix
max = np.max(data)
print(f"Max Value : {max}")

# Calculate average value of each column
avg_each_col = np.mean(data, axis=0)
print(f"Average val of each col : {avg_each_col}")