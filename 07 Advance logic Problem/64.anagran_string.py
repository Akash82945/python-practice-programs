def isAnagram(string1, string2):
    # LOGIC 1: Base Case Check
    # If the lengths of the two strings are different, they cannot be anagrams.
    # This check prevents unnecessary loops and improves efficiency.
    if len(string1) != len(string2):
        return False
    
    # LOGIC 2: Frequency Mapping (Balance Scale Logic)
    # We use a dictionary to keep track of the character counts (the 'balance').
    count_char = {}
    
    for i in range(len(string1)):
        # Increment the count for the character found in string1 (Add weight)
        char1 = string1[i]
        count_char[char1] = count_char.get(char1, 0) + 1
        
        # Decrement the count for the character found in string2 (Remove weight)
        char2 = string2[i]
        count_char[char2] = count_char.get(char2, 0) - 1
        
    # LOGIC 3: Final Balance Verification
    # If the strings are anagrams, every value in the dictionary must be exactly 0.
    # This is because every +1 from string1 should have a matching -1 from string2.
    for count in count_char.values():
        if count != 0:
            # If any count is not zero, the characters do not match perfectly.
            return False
    
    # If all counts are zero, the strings are perfect anagrams!
    return True

# --- Testing ---
string1 = "Silent".lower()
string2 = "Lisent".lower()

result = isAnagram(string1, string2)
print(f"Strings are Anagram: {result}")