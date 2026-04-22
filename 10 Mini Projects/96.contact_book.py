def contact_book():
    
    contacts = []
    
    while True:
        
        print("\n1. View all Contact.\n2. Add Contact.\n3. Search Contact.\n4. Delete Contact.\n5. Edit Contact.\n6. Exit.")
        
        try:
            choise = int(input("Enter your Choise : "))
        except ValueError:
            print("Please Choose into 1-5.")
            
        if choise == 1:
            if not contacts:
                print("Contact is Empty.")
                continue
            contacts.sort(key=lambda x: x['name'])
            for i,c in enumerate(contacts, 1):
                print(f"{i} {c['name']} | {c['phone']} | {c['email']}")
            
        elif choise == 2:
            
            name = input("Enter Customer Name : ")
            phone = input("Enter Customer Phone no : ")
            is_duplicate = any(c['phone'] == phone for c in contacts)
            if is_duplicate:
                print("This phone number already Exist.")
                continue
            if len(phone) != 10:
                print("Invalid Number.")
                continue
            
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
            del_name = input("Enter name to delete Contact : ").lower()
            matches = [c for c in contacts if c['name'].lower() == del_name]
            
            if not matches:
                print("No contant found.")
            elif len(matches) == 1:
                contacts.remove(matches[0])
                print("Deleted!")
            else:
                print(f"\nMultiple {del_name} found. Which Contant delete?")
                for i,m in enumerate(matches, 1):
                    print(f"{i} {m['name']} | {m['phone']} | {m['email']}")
                    
                pick = int(input("Enter Number : ")) -1
                contact.remove((matches[pick]))
                print("Selected contact is Deleted.")
            
        elif choise == 5:
            update_contact = input("Enter name ").lower()
            matches = [c for c in contacts if c['name'].lower() == update_contact]
            
            if not matches:
                print("No Contant to Changed anything.")
            elif len(matches) == 1:
                target = matches[0]
                print(f"Updating : {target['name']}")
                choose_input = input("Choose Which you can edit (phone/email): ").lower()
                if choose_input == "phone":
                    target['phone'] = input(f"Enter new phone (Current phone {target['phone']}) : ")
                    print("Updated Successfully.")
                    
                elif choose_input == 'email':
                    target['email'] = input(f"Enter new email (Current Email {target['email']}) : ")
                    print("Updated Successfully.")
                    
                else:
                    print("choose first to which you can edit.")
            else:
                print(f"\nMultiple Matches found for '{update_contact}'")
                for i,m in enumerate(matches, 1):
                    print(f"{i}.{m['name']} | {m['phone']} | {m['email']}")
                
                try:
                    pick = int(input("\nChoose the number to update (or 0 to cnacle) : ")) -1
                    if 0 <= pick < len(matches):
                        target = matches[pick]
                        # choose_input = input("Choose Which you can edit (phone/email): ").lower()
                        if choose_input == "phone":
                            target['phone'] = input(f"Enter new phone (Current phone {target['phone']}) : ")
                            print("Updated Successfully.")
                            
                        elif choose_input == 'email':
                            target['email'] = input(f"Enter new email (Current Email {target['email']}) : ")
                            print("Updated Successfully.")
                        
                        else:
                            print("choose first to which you can edit.")
                    else:
                        print("Updated Cancelled.")
                except ValueError:
                    print("Invalid Input. Update Failed.")
        
        elif choise == 6:
            print("Good Bye!👋")
            break
        
        else:
            print("Invalid choise.")
            
contact_book()