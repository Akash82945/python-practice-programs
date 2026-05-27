import json
from pathlib import Path


# Store Employee records
file_path = Path(r"C:\Users\LENOVO\Desktop\Practice set\python-practice-programs\11 Python Library\8 JSON Library\Employe.json")
file_path.parent.mkdir(parents=True,exist_ok=True)

emp_data = {
    'ID' : 101,
    'Name' : 'Akash',
    'Dept' : 'AIML',
    'Salary' : 53000
}


# Buit in Function
file_path.write_text(json.dumps(emp_data, indent=4))
# with open(file_path,'w') as file:
#     json.dump(emp_data,file,indent=4)

# Buit in Function
loaded_data = json.loads(file_path.read_text())
# with open(file_path,'r') as file:
    # loaded_data = json.load(file)

print(loaded_data)
print(json.dumps(loaded_data,indent=4))






# OOPs Format Code
# class Employee():
    
#     def __init__(self,id,name,dept,salary):
#         self.id = id
#         self.name = name
#         self.dept = dept
#         self.salary = salary
    
#     def emp_info(self):
#         return {
#         'Employee_ID' : self.id,
#         'Employee_Name' : self.name,
#         'Employee_Dept' : self.dept,
#         'Employee_Salary' : self.salary
#         }
    
     
        
# class EmployeeManager():
    
#     def __init__(self,file_path):
#         self.file_path = Path(file_path)
#         self.file_path.parent.mkdir(parents=True,exist_ok=True)
        
        
#     def _load_data(self):
#             if self.file_path.exists() and self.file_path.stat().st_size>0:
#                 return json.loads(self.file_path.read_text())
#             return []
        
#     def _save_data(self,data):
#             self.file_path.write_text(json.dumps(data,indent=4))
            
        
#     def add_employee(self,employee_obj):
#         employees = self._load_data()
        
#         for emp in employees:
#             if str(emp['Employee_ID']) == str(employee_obj.id):
#                 print(f"\nError! {employee_obj.id} is already Exists.\n")
#                 return False
        
#         employees.append(employee_obj.emp_info())
#         self._save_data(employees)
#         print(f'Done {employee_obj.name}')
            
        
#     def display_all(self):
#         employees = self._load_data()
#         if not employees:
#             print("Data not found.")
#             return
            
#         print('\n'+'+'*40+'\n----- Store Employee Records -----')
#         for emp in employees:
#             print(f'''
#             \nEmployee Details
#             ID : {emp['Employee_ID']}
#             Name : {emp['Employee_Name']}
#             Dept : {emp['Employee_Dept']}
#             Salary : {emp['Employee_Salary']}
#             ''')
#         print('-'*50)
                
    
# path_string = r"C:\Users\LENOVO\Desktop\Practice set\python-practice-programs\11 Python Library\8 JSON Library\employee_records.json"
# manager = EmployeeManager(path_string)

# while True:
#     print("\nEnter new employees details.")
#     print("Enter (q) in Emp Id for exit.\n")
    
#     emp_id = input("Enter Emp ID : ")
#     if emp_id.lower() == 'q':
#         break
    
#     name = input("Enter name: ")
#     dept = input("Enter Department : ")
#     try:
#         salary = int(input("Enter Salary : "))
#     except ValueError:
#         print("Please Enter Valid salary.")
#         continue

#     new_emp = Employee(emp_id,name,dept,salary)

#     manager.add_employee(new_emp)

# manager.display_all()