import numpy as np


# # # Task 1 : Create dataset of marks using array
# # # 3D marks array whick row represent students and column represent subjects
# # marks = np.array([78,87,48,45,57,88,57,68,69,95,75,96,87,69,75,98,76,65,24,33,43,35,68,68,67])
# # marks_matrix = marks.reshape(5,5)
# # print("=== Dataset of student marks using array. ===")
# # print(f"Marks : \n{marks_matrix}")



# # # Task 2 : Find highest & lowest score
# # highest_marks = np.max(marks_matrix, axis=1)
# # lowest_marks = np.min(marks_matrix, axis=1)
# # print(f"Highest Marks : {highest_marks}")
# # print(f"Lowest Marks : {lowest_marks}")



# # Task 3 : Generate random dataset
# random_dataset = np.random.randint(30,90,25)
# print(f"Random dataset : {random_dataset}")



# # Task 5 : Reshape Dataset into matrix
# matrix_dataset = random_dataset.reshape(5,5)
# print(f"Random Dataset Matrix : \{matrix_dataset}")



# Task 7 : Compute dot product for ML concept
a = np.array([23,43,65,23,43])
b = np.array([12,43,12,65,87])
bias = 10

dot_of_ab = np.dot(a,b) + bias
print(dot_of_ab)



# Rows = Days (Mon, Tue), Columns = Items (Item A, Item B, Item C)
sales = np.array([
    [10, 5, 2],  # Monday sales quantities
    [4,  8, 1]   # Tuesday sales quantities
])

# Column vector representing the price for Item A, Item B, and Item C
prices = np.array([
    [1.50],  # Item A price
    [2.00],  # Item B price
    [5.00]   # Item C price
])

matrix_dot = sales @ prices
print(matrix_dot)

relu = np.maximum(0,matrix_dot)
print(f"relu : {relu}")

sig = 1 / (1 + np.exp(-(matrix_dot)))
print(f"sig : {sig}")