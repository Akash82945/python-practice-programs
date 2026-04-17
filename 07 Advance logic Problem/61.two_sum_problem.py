# Using nested loops

# n = int(input("Enter lenght of array: "))
# my_array = []
# for i in range(n):
#     i = int(input("Enter values: "))
#     my_array.append(i)
 
# print(my_array)

# number = my_array

# def sum_two_number(number):
    
#     target = 0
    
#     for i in range(number):
#         for j in range(i+1, number):
#             if j+i == target:
#                 target = i+j
#     return target
 
# print(sum_two_number(number))   
     
  


# Using Hash map  
def sum_two_number(my_array, target):
    seen_number = {}
    
    for i in range(len(my_array)):
        curent_value = my_array[i]
        required = target-curent_value
    
        if required in seen_number:
            return [seen_number[required],i]
        seen_number[curent_value]= i
    return "no pair"

n = int(input("Enter lenght of array: "))
my_array = []
for i in range(n):
    i = int(input(f"Enter value {i}: "))
    my_array.append(i)
    
target = int(input("Enter Target: "))

result = sum_two_number(my_array, target)

print(result)





# # Using two pointer
# def sum_two_number(my_array, target):
    
#     left = 0
#     right = len(my_array)-1
    
#     while left < right:
#         current_sum = my_array[left] + my_array[right]
        
#         if current_sum == target:
#             return (f"Pair found {my_array[left]} and {my_array[right]}")
        
#         elif current_sum < target:
#             left +=1
            
#         else:
#             right -=1
            
#     return "Pair not Found"

# my_array = input("Enter Values of array: ")

# new_array = [int(x) for x in my_array.split()]

# target = int(input("Enter Target: "))

# result = sum_two_number(new_array,target)

# print(result)