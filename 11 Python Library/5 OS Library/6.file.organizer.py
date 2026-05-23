import os

# File organizer

print(" ===== File Organizer Automation. =====")
target_path = r"C:\Users\LENOVO\Downloads"

file_type = {
    'Images' : ['.jpg','.png','.jpeg'],
    'Videos' : ['.mp4','.mvk'],
    'Documents' : ['.pdf','.txt','.docx','.xlsx'],
    'Audio' : ['.mp3','.wav'],
    'Presentations' : ['.ppt', '.pptx']
}

for file in os.listdir(target_path):
    file_path = os.path.join(target_path,file)
    
    if os.path.isfile(file_path):
        _,extension = os.path.splitext(file)
        
    for folder_name,extensions in file_type.items():
        if extension.lower() in extensions:
            subfolder_path = os.path.join(target_path,folder_name)
            
            if not os.path.exists(subfolder_path):
                os.makedirs(subfolder_path)
            
            os.rename(file_path,os.path.join(subfolder_path,file))
            
print("File Organize Successfully.")


