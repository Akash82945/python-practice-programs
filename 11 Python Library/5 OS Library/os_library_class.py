import os


# Current Folder Check
# folder = os.getcwd()
# print('Current Working Folder = ',folder)


# List all files
# files = os.listdir()
# print(f'List of all files : {files}')
# for file in files:
#     print(f'List of all files : {file}')



# Create new folder
# new_folder = os.mkdir("pythonfiles")
# print(f"Folder Create Successfully.")    



# Delete Folder
target_folder = r"C:\Users\LENOVO\Desktop\Practice set\Python_file0123"
if os.path.exists(target_folder):
    del_folder = os.rmdir(target_folder)
    print("Folder delete successfully.")
else:
    print("Folder not Found.")
    
# def_folder = os.rmdir("Pytho_File0123")
# print("Folder Delete Successfully.")



# Rename files
# rename = os.rename('09 Opps','09 OPPs')
# print("Name changed successfully.")