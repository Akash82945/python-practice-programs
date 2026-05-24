import shutil

# Create Backup folder
# shutil.copy("Programing_history","Backup_programing_history")
# print("Done!")



# Create Backup folder another dictonary
import os
target_path = r"C:\Users\LENOVO\Desktop\DAA in C"
destination = r"C:\Users\LENOVO\Desktop"
backup_path = os.path.join(destination,"Backup_DAA in C")
shutil.copytree(target_path,backup_path,dirs_exist_ok=True)
print("Done!")