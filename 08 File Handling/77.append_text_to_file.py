def append_text(text):
    
    with open ("File Handling/Note.txt", "a") as file:
        content = file.write("\n"+text)
        
    return "Append text is Successfully."        

text = input("Enter data: ")

print(append_text(text))