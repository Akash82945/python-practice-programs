def rotate_list(my_array, k):
    n = len(my_array)
    
    # Step 1: Handle empty list to avoid ZeroDivisionError
    if n == 0:
        return my_array
        
    # Step 2: Normalize k (e.g., rotating 5 items by 6 is the same as rotating by 1)
    k = k % n
    
    # Step 3: Logic for rotation
    if k == 0:
        # No rotation needed if k is 0 or a multiple of n
        return my_array
    
    else:
        # Part 1: Take the last 'k' elements using negative slicing
        # Example: for [1, 2, 3, 4, 5] and k=2, part1 is [4, 5]
        part1 = my_array[n-k:]
        
        # Part 2: Take all elements from the start up to index n-k
        # Example: part2 is [1, 2, 3]
        part2 = my_array[:n-k]
        
        # Step 4: Concatenate the two parts to get the rotated list
        # We return this directly instead of appending it to another empty list
        rotated_result = part1 + part2
        
        return rotated_result

# --- Execution ---
my_input = input("Enter values of array separated by space: ")
k_input = int(input("Enter value of k: "))

# Converting the space-separated string into a list of integers
new_array = [int(x) for x in my_input.split()]

result = rotate_list(new_array, k_input)

print(f"Rotated List: {result}")