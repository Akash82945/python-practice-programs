import json
from pathlib import Path

# Student json data

file_path = Path(r"C:\Users\LENOVO\Desktop\Practice set\python-practice-programs\11 Python Library\8 JSON Library\student_data.json")
file_path.parent.mkdir(parents=True, exist_ok=True)

student_data = {
    'Name' : 'Akash Kumar',
    'Branch' : '(AIML)',
    'Roll No' : 2304324,
    'Course' : 'B-Tech'
}

# with open(file_path, "w") as file:
#     json.dump(student_data,file,indent=4)
    

file_path.write_text(json.dumps(student_data,indent=4))

if file_path.exists():
    print("Successfully Created Student JSON Data.")


