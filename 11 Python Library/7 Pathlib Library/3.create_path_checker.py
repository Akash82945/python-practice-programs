from pathlib import Path
import os


# Create Path checker tool

print('===== Path checker Tool =====')

def path_checker():
    desktop_path = Path(r"C:\Users\LENOVO\Desktop")
    download_path = Path(r"C:\Users\LENOVO\Downloads")
    document_path = Path(r"C:\Users\LENOVO\Documents")
    
    main_path = [
        "Select Any one as [1/2/3]: ",
        'Desktop [1]',
        'Downloads [2]',
        'Documents [3]'
    ]
    # print(main_path); 
    for x in main_path:
        print(x)
    user_input = int(input("Enter Your choise: "))
    
    if user_input == 1:
        base_path = desktop_path
        
    elif user_input == 2:
        base_path = download_path
        
    elif user_input == 3:
        base_path = document_path
        
    else:
        print("Please Enter Valid path.")
    
    next_path = input("Enter file or folder name : ").strip()
    target_path = base_path/next_path
    
    if not target_path.exists():
        print("File does not exist.")
        return
    
    if target_path.is_file():
        
        print('\nFull file name : ',target_path.name)
        print('File extension : ',target_path.suffix)
        print('File name : ',target_path.stem)
        
    elif target_path.is_dir():
        file_count = len(list(target_path.iterdir()))
        print('Number of files : ',file_count)
    
path_checker()