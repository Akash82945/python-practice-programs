def frequency_of_element(string):
    # Step 1: Initialize an empty dictionary to act as a frequency map.
    # The dictionary will store characters as 'keys' and their counts as 'values'.
    seen = {}
    
    # Step 2: Traverse through every character in the input string.
    for char in string:
        # Check if the character has already been recorded in our 'seen' dictionary.
        if char in seen:
            # If the character exists, increment its current count by 1.
            seen[char] = seen[char] + 1 
            
        else:
            # If the character is encountered for the first time,
            # initialize its frequency count to 1.
            seen[char] = 1
            
    # Step 3: Return the final dictionary containing the frequency of each element.
    return seen

# --- Execution ---
user_string = input("Enter string: ")

# Calling the function and storing the frequency results.
result = frequency_of_element(user_string)


print("\n--- Character Frequencies ---")

# Step 3: Iterate through dictionary items to print line by line.
# .items() returns both the key (character) and the value (frequency).
for char, count in result.items():
    # Using an f-string for a clean, formatted output
    print(f"'{char}': {count}")