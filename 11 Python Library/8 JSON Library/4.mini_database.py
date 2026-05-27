import json
from pathlib import Path
import os


# Create Json Mini Projects

class MiniDB:
    
    def __init__(self,filename='db.json'):
        self.filename = filename
        self.data = self._load_data()
        
    def _load_data(self):
        if not os.path.exists(self.filename):
            return {}
        try:
            with open(self.filename,'r', encoding='utf-8') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Warning! new file open soon...")
            return {}
        
    def _save_data(self):
        with open(self.filename,'w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)
        
    
    def create(self, key, value):
        if key in self.data:
            print(f"Error! {key} This data is already exist.")
            return False
        
        self.data[key] = value
        self._save_data()
        return True
    
    def read(self, key=None):
        if key is None:
            return self.data
        return self.data.get(key, "Error, Deata not found.")
    
    
    def update(self, key, new_value):
        if key not in self.data:
            print(f"Error! {key} Data Not found.")
            return False
        
        self.data[key] = new_value
        self._save_data()
        return True
    
    def delete(self, key):
        if key in self.data:
            del self.data[key]
            self._save_data()
            return True
        print(f'Error {key} data not found')
        return False
    
    

file_path = r"C:\Users\LENOVO\Desktop\Practice set\python-practice-programs\11 Python Library\8 JSON Library\data.json"

db = MiniDB(file_path)

print("===== Mini Database =====")

while True:
    print('''
          1. Show Database.
          2. Create Database.
          3. Update Database.
          4. Delene Data.
          5. Exit 
          ''')
    try:
        user_input = int(input("\nChoose Your Option [1/2/3/4/5] : "))
    except ValueError:
        print("Please Enter valid choise.")
    if user_input == 1:
        print('---Current Database---')
        current_data = db.read()
        if not current_data:
            print('Database is Empty.')
        else:
            print(json.dumps(current_data,indent=4, ensure_ascii=False))
    
    elif user_input == 2:
        print('---Create New Entry---')
        key = input('Enter key (eg. user_101): ').strip()
        name = input('Enter name : ').strip()
        role = input("enter role : ").strip()
        value = {'name' : name, 'role' : role}
        db.create(key,value)
        print('\n')
        
    elif user_input == 3:
        print('---Update Data---')
        key = input("Enter key to update: ").strip()
        
        if key in db.read():
            name = input("Enter new name: ").strip()
            roll = input("Enter new role: ").strip()
            value = {'name' : name, 'roll' : roll}
            db.update(key,value)
        else:
            print(f'Key {key} not found.')
            
    elif user_input == 4:
        print('---Delete Data---')
        key = input("Enter key to Delete: ").strip()
        db.delete(key)
        
    elif user_input == 5:
        print("Thankyou for using MINI Database.")
        break
    
    else:
        print("Invalid Choise! Please Choose Right Opthon.")
        
        