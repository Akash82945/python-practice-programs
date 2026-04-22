def contact_book():
    
    contacts = []
    
    while True:
        
        print("\n1. View all Contact.\n2. Add Contact.\n3. Search Contact.\n4 .Delete Contact.\n5. Exit.")
        
        try:
            choise = int(input("Enter your Choise : "))
        except ValueError:
            print("Please Choose into 1-5.")
            
        if choise == 1:
            if not contacts:
                print("Contact is Empty.")
            for i,c in enumerate(contacts, 1):
                print(f"{i} {c['name']} | {c['phone']} | {c['email']}")
            
        elif choise == 2:
            name = input("Enter Customer Name : ")
            phone = int(input("Enter Customer Phone no : "))
            email = input("Enter Customer Email : ")
            contacts.append({"name" : name , "phone" : phone , "email" : email})
            print("\nContact added successfully.")
            
        elif choise == 3:
            search = input("Search by Name : ").lower()
            found = False
            
            for contact in contacts:
                if search in contact['name'].lower():
                    print(f"Found: {contact['name']} | {contact['phone']} | {contact['email']}")
                    found = True
            if not found:
                print("No Contact name matched in Contact book.")
                
        elif choise == 4:
            del_name = input("Enter name to delete Contact : ")
            contacts = [c for c in contacts if c['name'].lower() == del_name]
            print("Deleted Success.")
            
        elif choise == 5:
            print("Good Bye!👋")
            break
        
        else:
            print("Invalid choise.")
            
contact_book()