# file = open("Notes.txt" , "w")
# file.write(input("Enter Notes: "))
# file.close

#Create File Method function
print("Write your note in NOtes file.")
def create_file(new_file):
    file = open("File Handling/Note.txt" , "a")
    file.write("\n"+new_file)
    file.close()
    
    return "Successfully Write in the file."

new_file = input("enter data: ")
print(create_file(new_file))