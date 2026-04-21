def to_do_list():
    print(" ===== TO DO LIST =====")
    
    
    task = []
    
    while True:
        print("Choose what you want!")
        print('''
            1. Show Task
            2. Mark Task Done
            3. Add Task
            4. Delete Task
            5. Exit
            ''')
        choise = int(input("Enter Your Choise: "))
        if choise == 1:
            if not task:
                print("Empty Task.")
            for i in task:
                print(f"{i} {task}")
            print(f"Your Tasks.\n{task}")
        
        elif choise == 2:
            input_task = input("Enter Your Task : ")
            task.append(input_task)
            print("Task Added Successfully.")
            
        elif choise == 3:
            mark_done = int(input("Enter 1 for mark Done : "))
            task[mark_done]['Done'] = True
            print('Great Job!')
            
        
        elif choise == 4:
            remove_task = int(input("Enter Task no Which you Can delete: "))
            if remove_task in task:
                task.remove(remove_task)
                print("Task Removed Successfully.")
            else:
                print("Task is not present in List.")
                
        elif choise == 5:
            print("Good Bye!")
            break
        
        else:
            print("Invalid Choise.")
            
            
            
to_do_list()