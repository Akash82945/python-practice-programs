import os

# list all file from current folder
# files = os.listdir()
# for file in files:
#     print(file)
    



# list all file from another folder
target_folder = r"C:\Users\LENOVO\Documents"
files = os.listdir(target_folder)
for file in files:
    print(file)