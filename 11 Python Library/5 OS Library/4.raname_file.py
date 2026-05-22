import os

# Rename file in current directory
# target_file = r"C:\Users\LENOVO\Desktop\Practice set\python-practice-programs\11 Python Library\5 OS Library\New Folder"
# new_file = r"C:\Users\LENOVO\Desktop\Practice set\python-practice-programs\11 Python Library\5 OS Library\Akash Kumar"

# if os.path.exists(target_file):
#     os.rename(target_file,new_file)
# print('scussfully ranamed')
    




# Rename file in another folder
target_file = r"C:\Users\LENOVO\Desktop\Akash Kumar Sah"
new_file = r"C:\Users\LENOVO\Desktop\Akash Kumar"
if os.path.exists(target_file):
    os.rename(target_file,new_file)
print("Successful")