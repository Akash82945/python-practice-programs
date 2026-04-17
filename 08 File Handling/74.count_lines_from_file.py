def count_lines():

    with open ("File Handling/Note.txt" , "r") as file:
        
        lines = file.readlines()
        
        file.close() 
        
    # --- Manual Counter Logic ---
    # count = 0
    # for line in lines:
    #     count += 1
        
    return len(lines)
        
print(count_lines())