def longest_word_in_sentence(sentence):
    # Step 1: Tokenization. 
    # .split() scans the string for spaces and cuts it into a list of individual words.
    # "Python is fun" -> ["Python", "is", "fun"]
    new_sentence = list(sentence.split())    
    
    # Step 2: Initialize a "Champion" variable.
    # We start with an empty string so that the first word we encounter will always win.
    longest_word = ""
    
    # Step 3: Iterate through each word (token) in the list.
    for word in new_sentence:
        # Step 4: Comparison Logic (The "King of the Hill" strategy).
        # Compare the length of the current 'word' with our current 'longest_word'.
        if len(word) > len(longest_word):
            # If the current word is strictly longer, it becomes the new champion.
            longest_word = word
            
    # Step 5: After checking every word, return the final winner.
    return longest_word

# --- Execution ---
sentence = input("Enter sentence: ")

# Calling the function and displaying the result.
result = longest_word_in_sentence(sentence)
print(f"The longest word is: {result}")