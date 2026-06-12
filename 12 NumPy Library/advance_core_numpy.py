import numpy as np


# Modify the original data with slicing
# original = np.array([1,2,3,4,5])
# my_view = original[:3]
# my_view[0] = 99
# print(f"Original Data : {original}")
# print(f"My view : {my_view}")




# Modify the data but not affect the origin value using .copy()
# original = [1,2,3,4,5]
# my_view = original[:3].copy()
# my_view[0] = 99
# print(f"Original Data : {original}")
# print(f"My view : {my_view}")





# # Sensor Calibrations
# calibrations = np.array([10.5, 20.2, 30.8, 40.1])
# safe_calibrations = calibrations[:3].copy()
# safe_calibrations[0] = 0
# print(f"Original data : {calibrations}")
# print(f"Copy My view : {safe_calibrations}")





# # Fansing indexing
# items = np.array(["Apple", "Banana", "Cherry", "Date", "Elderberry"])
# indices = [0,1,4]
# selected_items = items[indices]
# print(selected_items)


# matrix = np.array([
#     [10, 10, 10],  # Row 0
#     [20, 20, 20],  # Row 1
#     [30, 30, 30],  # Row 2
#     [40, 40, 40]   # Row 3
# ])

# target_row = matrix[[3,0]]
# print(target_row)


# transactions = np.array([
#     [100, 101],  # Row 0
#     [200, 202],  # Row 1
#     [300, 303],  # Row 2
#     [400, 404],  # Row 3
#     [500, 505]   # Row 4
# ])

# target_row = transactions[[4,1,2]]
# print(target_row)






# Normal dot product in python
# A = np.array([[1, 2], [3, 4]])
# B = np.array([[2, 0], [1, 2]])
# dot = A * B
# print(dot)


# In modern python user [@ or np.dot()]
# Rows = Days (Mon, Tue), Columns = Items (Item A, Item B, Item C)
sales = np.array([
    [10, 5, 2], 
    [4,  8, 1]   
])

# Column vector representing the price for Item A, Item B, and Item C
prices = np.array([
    [1.50],  
    [2.00],  
    [5.00]   
])

dot_product = sales @ prices
# dot_product = np.dot(sales,prices)
print(dot_product)