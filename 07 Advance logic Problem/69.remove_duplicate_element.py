# def remove_duplicate_element(my_array):
    
#     uniqe_set = {}
    
#     duplicate_list = list(my_array)
    
#     for num in my_array:
#         if num in uniqe_set:
#             if num in duplicate_list:
#                 duplicate_list.remove(num)
        
#         else:
#             uniqe_set[num] = True
            
    
#     return duplicate_list

# my_array =  input("Enter arrays Values: ")
# new_array = [int(x) for x in my_array.split()]

# result = remove_duplicate_element(new_array)

# print(result)






def remove_duplicate_element(my_array):
    # Step 1: Initialize an empty dictionary (or set) to act as 'memory'.
    # Dictionaries allow for near-instant (O(1)) lookups to check if a number exists.
    uniqe_set = {}
    
    # Step 2: Initialize an empty list to store elements in their original order,
    # but without any repetitions.
    duplicate_list = []
    
    # Step 3: Iterate through every number in the input array.
    for num in my_array:
        # Check if the current number is NOT already in our 'memory' dictionary.
        if num not in uniqe_set:
            # If it's a new number, add it to our final result list.
            duplicate_list.append(num)
            
            # Record this number in our dictionary so we can recognize it if it appears again.
            uniqe_set[num] = True
            
    # Step 4: Return the list which now contains only the first occurrence of each element.
    return duplicate_list

# --- Execution ---
# Taking space-separated input from the user.
my_input = input("Enter array values: ")

# Converting the string of numbers into a list of integers.
new_array = [int(x) for x in my_input.split()]

# Calling the function and printing the result.
result = remove_duplicate_element(new_array)
print(f"List after removing duplicates: {result}")