from pathlib import Path
import time
import threading

# Create Path checker tool

print('===== Path checker Tool =====')

found_file = []

def perform_search(base_path,search_pattern):
    global found_file
    found_file = list(base_path.rglob(search_pattern))

def file_finder():
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
    
    
    search_pattern = input("enter file or folder or extension : ")
    
    
    task_thread = threading.Thread(target=perform_search,args =(base_path,search_pattern))
    task_thread.start()

    spinner = ['|','\\','-','/']
    idx = 0

    while task_thread.is_alive():
        print(f"\rSearching file.. {spinner[idx%len(spinner)]}",end="")
        idx += 1
        time.sleep(0.1)
        
    # print(f"\nSearching file {search_pattern}... Please wait!")
    
    found_file = list(base_path.rglob(search_pattern))
    
    if len(found_file) == 0:
        print("No file/folder not found.")
    else:
        print(f"\nToatal {len(found_file)} file(s) found.")
        
        print('-'*50)
        for idx,file in enumerate(found_file,start=1):
            file_size_kb = file.stat().st_size/1024
            print(f"{idx}. {file.name}")
            print(f"Location {file.parent}")
            print(f"Size : {file_size_kb:.2f}KB")
            print('-'*50)

file_finder()