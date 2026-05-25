from pathlib import Path


# Show File name or Extension 

file_path = r"C:\Users\LENOVO\Desktop\Practice set\python-practice-programs\11 Python Library\7 Pathlib Library\2.show_name_extension.py"
path = Path(file_path)
full_name = path.name
file_extension = path.suffix
only_name = path.stem

print(f'''
      Full name : {full_name}
      Extension : {file_extension}
      Only name : {only_name}
      ''')