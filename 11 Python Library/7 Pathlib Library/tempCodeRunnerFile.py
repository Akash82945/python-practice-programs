from pathlib import Path


# Create Path checker tool

print('===== Path checker Tool =====')

def path_checker():
    
    input_path = input("Enter Full Path : ")
    
    target_path = Path(input_path)
    
    if not target_path.exists():
        print("File does not exist.")
        return
    
    if target_path.is_file():
        
        print('Full file name : ',target_path.name)
        print('File extension : ',target_path.suffix)
        print('File name : ',target_path.stem)
        
    elif target_path.is_dir():
        file_count = len(list(target_path.iterdir()))
        print('Number of files : ',file_count)
    
path_checker()