def copy_content():
    
    with open ("File Handling/Note.txt", "r") as file:
        content = file.read()
        
        
    n_content = content
    
    with open ("File Handling/Copy_Note.txt", "w") as n_file:
        data = n_file.write(n_content)
        
    return "Content copy Scussfully."

print(copy_content())
         