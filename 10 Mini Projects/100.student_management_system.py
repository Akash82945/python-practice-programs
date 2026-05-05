import json
import os

def student_management_system():
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    file_path = os.path.join(script_dir, "Student Class.json")
    
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            try:
                student_class = json.load(file)
            except json.JSONDecodeError:
                student_class = []
    else:
        student_class = []
    
    while True:
        
        print(''''
        1. Show Student Details.
        2. Add Student.
        3. Update Students.
        4. Delete Student
        5. Exit
              ''')
        
        try:
            user_input = int(input("Enter your choice : "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if user_input == 1:
                        
            if not student_class:
                print("Student is not Found!")
                continue
            
            student_class.sort(key=lambda x: x['roll'])
            print("\n=====Student List=====")
            
            student_class.sort(key=lambda x: x['roll'])
            for i, s in enumerate(student_class, 1):
                print(f"{i} {s['roll']} | {s['name']} | {s['branch']} | {s['semester']} | {s['course']}")
                    
                    
        elif user_input == 2:
            roll = input("Enter Roll no : ").strip()
            
            is_duplicate = any(s['roll'] == roll for s in student_class )
            if is_duplicate:
                print("This Student is already exist in Class.")
                continue
            
            name = input("Enter Student name : ")
            branch = input("Enter your Branch : ")
            sem = input("Enter your Semester : ")
            course = input("Enter your Course : ")
            
            student_class.append({
                'roll' : roll,
                'name' : name,
                'branch' : branch,
                'semester' : sem,
                'course' : course
            })
            
            with open (file_path, 'w') as file:
                json.dump(student_class, file, indent=4)
        
            print("Added Successfully.")
        
        elif user_input == 3:
            updated_roll = input("Enter the Roll of the student to update: ").strip()
            student_found = False
            
            for s in student_class:
                if s['roll'] == updated_roll:
                    student_found = True
                    print(f"Updating details for {s['name']}. leave blank to keep current value.")
                    
                    new_name = input(f"Enter New Name ({s['name']}): ").strip()
                    new_branch = input(f"Enter New Name ({s['branch']}): ").strip()
                    new_sem = input(f"Enter New Name ({s['semester']}): ").strip()
                    new_course = input(f"Enter New Name ({s['course']}): ").strip()
                    
                    if new_name: s['name'] = new_name
                    if new_branch: s['breanch'] = new_branch
                    if new_sem: s['semester'] = new_sem
                    if new_course: s['course'] = new_course
                    
                    with open (file_path, "w") as file:
                        json.dump(student_class, file, indent=4)
                        
                    print("Updated Successfully")
                    break
                
                if student_found:
                    print("No Student found with that roll.")
                    
        
        elif user_input == 4:
            del_stu = input("Enter roll which student you delete : ")
            
            student_to_remove = None
            for s in student_class:
                if s['roll'] == del_stu:
                    student_to_remove = s
                    break
            
            if student_to_remove:
                student_class.remove(student_to_remove)
                with open(file_path, "w") as file:
                    json.dump(student_class,file,indent=4)
                print("Deleted Successfully.")
            else:
                print("No student found with that roll.")    
            
                
        elif user_input == 5:
            enter = input("Enter 'q' for quit : ").lower()
            
            if enter.lower() == 'q' :
                print("Good bye.")
                break
            
            
student_management_system()