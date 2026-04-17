# Function to read content from a file
def read_file():

    # Open the file in read mode ("r")
    # file = open("File Handling/Note.txt", "r")
    with open("File Handling/Note.txt" , "r") as file:

    # Read the entire content of the file and store it in 'content'
        content = file.read()

    # Close the file after reading to free system resources
    file.close()

    # Print success message after file is read
    print("File content read successfully.")

    # Return the file content
    return content


# Call the function and print the returned content
print(read_file())
