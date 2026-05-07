# Mini project of File Search
import os

def file_finder():
    print(" ===== Mini File Search Engine =====")
    
    dictonary = input("Enter folder name? (eg. C:/ or D:/) : ")
    filename_to_search = input("Enter File name : ").lower()
    
    if not os.path.exists(dictonary):
        print("Invalid Dictonary in your system.")
        return
    
    print(f"\nSearching for '{filename_to_search}' in {dictonary}...")
    
    found = False
    count = 0
    
    for root, dirs,files in os.walk(dictonary):
        for file in files:
            if filename_to_search in file.lower():
                full_path = os.path.join(root,file)
                print(f"Found : {full_path}")
                found = True
                count += 1
                
    if found:
        print(f"\nSearch complete! Total {count} files found.")
    else:
        print("Sorry file not found.")
        
if __name__ == "__main__":
    file_finder()