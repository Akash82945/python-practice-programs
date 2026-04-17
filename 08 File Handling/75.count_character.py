def count_character():
    with open ("File handling/Note.txt", "r") as file:
        content = file.read()
    
    file = content.strip()
    
    # count_char = []
    # for char in file:
    #     count_char.append(char)
    # return len(count_char)
    
    return len(file)
        
        
print(f"Characters in this file: {count_character()}")