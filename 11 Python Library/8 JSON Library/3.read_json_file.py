import json
from pathlib import Path


# Read Json file

file_path = Path(r"C:\Users\LENOVO\Desktop\Practice set\python-practice-programs\11 Python Library\8 JSON Library\data.json")

if file_path.exists():
    data = json.loads(file_path.read_text())
    print(json.dumps(data,indent=4))
else:
    print("File not found")

