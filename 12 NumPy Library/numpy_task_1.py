import numpy as np


# # Task 1 : Create dataset of marks using array
# # 3D marks array whick row represent students and column represent subjects
# marks = np.array([78,87,48,45,57,88,57,68,69,95,75,96,87,69,75,98,76,65,24,33,43,35,68,68,67])
# marks_matrix = marks.reshape(5,5)
# print("=== Dataset of student marks using array. ===")
# print(f"Marks : \n{marks_matrix}")



# # Task 2 : Find highest & lowest score
# highest_marks = np.max(marks_matrix, axis=1)
# lowest_marks = np.min(marks_matrix, axis=1)
# print(f"Highest Marks : {highest_marks}")
# print(f"Lowest Marks : {lowest_marks}")



# Task 3 : Generate random dataset
random_dataset = np.random.randint(30,90,25)
print(f"Random dataset : {random_dataset}")



# Reshape Dataset into matrix
matrix_dataset = random_dataset.reshape(5,5)
print(f"Random Dataset Matrix : \{matrix_dataset}")