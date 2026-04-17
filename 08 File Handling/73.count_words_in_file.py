def count_word():

    with open ("File Handling/Note.txt" , "r") as file:
        
        content = file.read()
        
    words = content.split()
    
    # --- Manual Accumulation (Commented Out) ---
    # count_word = []
    # for word in words:
    #     count_word.append(word)
    # Logic: This "Bucket Brigade" logic is redundant because 'words' 
    # is already the exact list we need.
        
    return len(words)

print(count_word())