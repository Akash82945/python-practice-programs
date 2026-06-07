import numpy as np


# Core Concept: ARRAy
# arr = np.array([2,3,4,5,6])
# print(arr)

# 1D array
# price = np.array([10.50, 20.00, 15.75])

# 2D array
# matrix = np.array([
#     [1,2,3],
#     [4,5,6]
# ])

# Generate Sequential number (like range)
# sequence = np.arange(0,12,2)

# Create array using default values
# zeros = np.zeros(5)
# ones = np.ones((2,4))

# Print All Arrays
# print(f'''
# 1D array : {price}\n
# 2D array : \n{matrix}\n
# Sequence array : {sequence}\n
# Default zero array : {zeros}\n
# Default ones array :\n {ones}
#       ''')


# Convert list to array
# data = [1,2,3,4,5]
# arr = np.array(data)
# print(arr)
# print('Type of Data : ',type(data))
# print('Type of Arr :',type(arr))




# All zero element Array
# arr = np.zeros(5)
# print(arr)


# Create Matrix
# arr = np.ones((3,3))
# print(arr)



# Create array Using range fun
# Real uae : Data simulation & Loop Replacement
# arr = np.arange(2,10,2)
# print(arr)



# Reshape Array
# Real use : Image data reshape & Ml Preprocessing
# arr = np.arange(6)
# new_arr = arr.reshape(2,3)
# print(new_arr)



# Find mean
# arr = np.array([20,23,23,553,53])
# arr_mean = np.mean(arr)
# print(f"Mean of Array : {arr_mean}")



# Sum of array
# arr = np.array([20,23,23,553,53])
# sum_arr = np.sum(arr)
# print(f"Sum of array ; {sum_arr}")



# Find min and max values
# arr = np.array([20,23,23,553,53])
# min = np.min(arr)
# max = np.max(arr)
# print(f"Minimum Value : {min}")
# print(f"Maximum Value : {max}")




# Create randmon data
# use : AI data simulation
# arr = np.random.rand(3)
# arr = np.random.randint(1,50,3)
# print(arr)



# Dot product
# a = np.array([1,2])
# b = np.array([3,4])
# print(np.dot(a,b))

# a = np.random.randint(1,12,size=3)
# b = np.random.randint(1,12,size=3)
# c = np.random.randint(1,12,size=3)
# print(a)
# print(b)
# print(c)
# ab_dot = np.dot(a,b)
# abc_dot = ab_dot*c
# ab_dot = np.cross(a,b)
# abc_dot = np.dot(np.cross(a,b),c)
# print(ab_dot)
# print(abc_dot)





# Create 3D matrix
# data = [1,2,3,4,5,6,7,8,9,10,11,12]
# arr = np.array(data)
# matrix = arr.reshape(2,2,3)
# print(matrix)

# Using random value
# matrix_3d = np.random.randint(1,121,size=(3,2,4))
# print(matrix_3d)



# Create Dice simulator using numpy
# while True:
#     dice = np.random.randint(1,7)
#     user_input = input("Press 'enter' to continue & press 'q' for quiet : ")
#     if user_input == "":
#         print(f"Dice no : {dice}")
#     elif user_input == 'q':
#         break
#     else:
#         print('Error')
        
        
        

# Create Array fron -10 to +10
# arr = np.random.randint(-10,11,4)
# print(arr)       




# Choise function
# coin = ['head','tail']
# coin_result = np.random.choice(coin, size=5)
# print(f"Coin result : {coin_result}")




# Shuffle function
# color = ['Red', 'Yellow', 'Orange', 'Pink']
# shuffl_color = np.random.shuffle(color)
# print(color)




# Random randn function
# normal_data = np.random.randn(2,3)
# print('Normal distribution data : \n',normal_data)




# Rock Paper Scisor
# game = ['Rock', 'Paper', 'Scisors']
# games = np.random.choice(game)
# print(games)




# Shuffling List
# list1 = np.random.randint(10,50,size=5)
# np.random.shuffle(list1)
# print(list1)




