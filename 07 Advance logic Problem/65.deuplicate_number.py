def duplicate_number(my_array):
    # Step 1: Initialize an empty dictionary to act as our 'memory'.
    # A dictionary provides O(1) average time complexity for lookups.
    seen = {}
    
    # Step 2: Initialize an empty list to store the duplicate values we find.
    duplicate = []
    
    # Step 3: Iterate through each number in the input array
    for num in my_array:
        # Check if the current number has been encountered before
        if num in seen:
            # If seen before, check if it's already recorded in the duplicates list.
            # This prevents adding the same number multiple times (e.g., [1, 1, 1]).
            if num not in duplicate:
                duplicate.append(num)
        else:
            # If it's the first time seeing this number, add it to the 'seen' dictionary.
            # We map the number as a key with a value of True to mark its presence.
            seen[num] = True
            
    return duplicate

# --- Execution ---
# Getting input from the user as a space-separated string
my_array_input = input("Enter Values for array: ")

# Using list comprehension to convert the input string into a list of integers
new_array = [int(x) for x in my_array_input.split()]

# Calling the function and storing the result
result = duplicate_number(new_array)

# Displaying the final list of duplicate values found
print(f"Duplicate values in this array: {result}")