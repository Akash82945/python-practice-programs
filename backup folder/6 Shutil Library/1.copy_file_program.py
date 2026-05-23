import shutil


# Copy file Programs
target_path = '11 Python Library'
copy_folder = shutil.copytree(target_path,'backup folder')
print('Done')