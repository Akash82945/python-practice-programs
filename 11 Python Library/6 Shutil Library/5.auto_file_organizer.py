import os
import shutil

target_dit = r"C:\Users\LENOVO\Downloads"

file_type = {
    'Compresed File' : ['.exe','.rar','.zip'],
    'Python File' : ['.py'],
    'C/C++ file' : ['.c','.cpp']
}


def file_organizer(folder_path):
    
    if not os.path.exists(folder_path):
        print("Error file does not exitst.")
        return
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path,filename)
        
        if os.path.isfile(file_path):
            _,file_extension = os.path.splitext(filename)
            file_extension = file_extension.lower()
            
            moved = False
            
            for folder_name, extensions in file_type.items():
                if file_extension in extensions:
                    dest_folder = os.path.join(folder_path,folder_name)
                    
                    os.makedirs(dest_folder,exist_ok=True)
                    
                    shutil.move(file_path, os.path.join(dest_folder,filename))
                    break
                
                
    print("File organizer Done!")
            
file_organizer(target_dit)