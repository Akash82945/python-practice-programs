import json


# student_data = {
#     'name' : "Akash Kumar",
#     'age' : 22,
#     'skills' : ['Python','Data Structure'],
#     'is_certified' : True
# }
# print("--- 1. Python Dict convert to Json string (dumps) ---")
# json_string = json.dumps(student_data,indent=4)
# print(json_string)
# print(type(json_string))


# parsed_dict = json.loads(json_string)
# print(parsed_dict)
# print(type(parsed_dict))

from pathlib import Path

file_path = Path(r"C:\Users\LENOVO\Desktop\Practice set\python-practice-programs\11 Python Library\8 JSON Library\data.json")
file_path.parent.mkdir(parents=True,exist_ok=True)

data = {
    'name' : 'Rahul',
    'age' : 22
}

info_data = {
    "username" : "coder_lenovo",
    "score" : 90,
    'active' : True
}

combine_data = {**data,**info_data}

with open (file_path,'w') as file:
    json.dump(combine_data,file,indent=4)

print(f"file Save Successfully {file_path.name}")

with open(file_path,'r') as file:
    loaded_data = json.load(file)

print(loaded_data)
print(loaded_data['score'])
print(json.dumps(loaded_data,indent=4))