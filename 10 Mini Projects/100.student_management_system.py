def student_management_system():
    
    student_class = []
    
    while True:
        
        print(''''
              1. Show Student Details.
              2. Add Student.
              3. Update Students.
              4. Delete Student
              5. Exit
              ''')
        
        user_input = input("Enter your choice : ")
    
        if user_input == 1:
            if not student_class:
                print("Student is not Found!")
                continue
            student_class.sort(key=lambda x: x['roll'])
            for i, s in enumerate(student_class, 1):
                print(f'{i} {s['roll']} | {s['name']} | {s['branch']} | {s['sem']} | {s['course']}')
                    
        elif user_input == 2:
            roll = input("Enter Roll no : ")
            name = input("Enter Student name : ")
            branch = input("Enter your Branch : ")
            sem = input("Enter your Semester : ")
            course = input("Enter your Course : ")
            
            student_class.append({'roll' : roll , 'name' : name , 'branch' : branch , 'semester' : sem , 'course' : course})
            
            is_duplicate = any(s['roll'] == roll for s in student_class )
            if is_duplicate:
                print("This Student is already exist in Class.")
                continue
        
            print("Added Successfully.")
        
        elif user_input == 3:
            pass
        
        elif user_input == 4:
            del_stu = input("Enter roll which student you delete : ")
            
            match = [s for s in student_class if s['roll'] == del_stu]
            
            if not match:
                print("No student is found.")
            else:
                student_class.pop
                print("Delete Successfully.")
                
        elif user_input == 5:
            enter = input("Enter 'q' for quit : ").lower()
            
            if enter.lower() == 'q' :
                print("Good bye.")
                break
            
            
student_management_system()