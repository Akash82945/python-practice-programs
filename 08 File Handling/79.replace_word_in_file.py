def replace_word(old_word, new_word):
    
    

    with open("File Handling/Note.txt", "r") as file:

        content = file.read()

        

    data = content

    

    if old_word in data:

        updated = data.replace(old_word , new_word)        

    else:

        return "Word not found."

    

    with open("File Handling/Note.txt", "w") as file:

        file.write(updated)

        

    return "Replacement Successful."

        

old_word = input("Enter Word which is replace in file: ")

new_word = input("Enter new word: ")

print(replace_word(old_word,new_word))