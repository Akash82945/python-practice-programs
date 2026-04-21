def to_do_list():
    print(" \n===== TO DO LIST =====")
    
    
    task = []
    
    while True:
        
        print("\nChoose what you want!")
        print('''
            1. Show Task
            2. Add Task
            3. Mark Task Done
            4. Delete Task
            5. Exit
            ''')
        
        try :
            choise = int(input("Enter Your Choise: "))
        except ValueError:
            print("Please Enter a number (1-5)")
            continue
        
        if choise == 1:
            if not task:
                print("Empty Task.")
            for i,t in enumerate(task, 1): 
                status = '✔' if t['done'] else " "
                print(f"{i } [{status}] {t['Task']}")

        
        elif choise == 2:
            input_task = input("Enter Your Task : ")
            task.append({"Task": input_task , "done":False})
            print("Task Added Successfully.")
            
        elif choise == 3:
            if not task:
                print("Nothig to Mark as done.")
                continue
            idx = int(input("Enter Task no to mark Done: ")) -1
            if 0 <= idx < len(task):
                task[idx]['done'] = True
                print("Great Job!")
            else:
                print("Invalid Task NO.")
            
        
        elif choise == 4:
            if not task:
                print("Nothing to Delete")
                continue
            
            idx = int(input("Enter Task no to delete: ")) -1
            if 0 <= idx < len(task):
                removed = task.pop(idx)
                print(f"Removed : {removed['Task']}")
            else:
                print("Invalid task NO. ")
                
        elif choise == 5:
            print("Good Bye!")
            break
        
        else:
            print("Invalid Choise.")
            
            
to_do_list()