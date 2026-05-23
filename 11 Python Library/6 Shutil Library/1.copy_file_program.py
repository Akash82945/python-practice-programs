import shutil


# Copy file Programs
# target_path = '11 Python Library'
# copy_folder = shutil.copytree(target_path,'backup folder')
# print('Done')



# Copy file programs from another directory
target_path = r"C:\Users\LENOVO\Documents\DSA in C"
copy_file = shutil.copytree(target_path,"DSA with C Language Copy")
print('Done')


# Copy in another dictonary 
# import os
# target_path = r"C:\Users\LENOVO\Documents\DSA in C"
# copy_path = r"C:\Users\LENOVO\Documents"
# final_destination = os.path.join(copy_path,"DSA with C Language Copy")
# copy_file = shutil.copytree(target_path,final_destination)
# print('Done')