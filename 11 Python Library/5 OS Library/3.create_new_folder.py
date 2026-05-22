import os

# Create new folder in current directory
# new_fol = os.mkdir('11 Python Library/5 OS Library/New Folder')
# print("Successfully Created new Folder")




# Create new folder in another directory
target_folder = r"C:\Users\LENOVO\Desktop"
new_folder = os.path.join(target_folder,"Akash Kumar Sah")
os.mkdir(new_folder)
print("Successfully Created new Folder")
