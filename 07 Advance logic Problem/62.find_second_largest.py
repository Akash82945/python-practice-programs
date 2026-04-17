def second_largest_number(my_array):
    # Step 1: Initialize both with the smallest possible value (Negative Infinity)
    # This ensures the logic works correctly even with negative numbers in the array.
    largest = float("-inf")
    second_largest = float("-inf")
    
    # Step 2: Iterate through every number in the array
    for num in my_array:
        # Case A: If the current number is greater than the current 'largest'
        if num > largest:
            # The previous 'largest' now becomes the 'second_largest'
            second_largest = largest
            # The current number takes the position of the new 'largest'
            largest = num
            
        # Case B: If the current number is smaller than 'largest' but greater than 'second_largest'
        # We also ensure the current number is not equal to 'largest' to handle duplicates.
        elif num > second_largest and num != largest:
            # Only update the 'second_largest' variable
            second_largest = num
    
    return second_largest

# --- Execution ---
user_input = input("Enter values of array (space separated): ")
# Converting the input string into a list of integers
new_array = [int(x) for x in user_input.split()]

result = second_largest_number(new_array)

# Logic to handle cases where a second largest doesn't exist (e.g., [10, 10, 10] or single element)
if result == float("-inf"):
    print("There is no second largest number.")
else:
    print(f"The second largest number in the array is: {result}")