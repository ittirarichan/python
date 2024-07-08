contacts={}
print("Customer Detail Book")
while True:
    print("\n1. Add a Contact")
    print("2. Display Contacts")
    print("3. Update contacts" )
    print("4. Remove a Contact")
    print("5. Search for a Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")
    if choice=='1':
        name=input("Enter contact name: ")
        number=input("Enter contact number: ")
        email=input("Enter Email id: ")
        dob=input("Enter your date of birth: ")
        place=input("Enter your place: ")
        contacts[name]=number
        print("{} added to contacts.".format(name))
    elif choice=='2':
        if not contacts:
            print("No contacts found.")
        else:
            print("\nContacts:")
            for name, number in contacts.items():
                 print("{:<20}{:<15}{:<30}{:<15}{:<20}".format(name, number, email, dob, place))
    elif choice == "3":
            name = input("Enter name to update: ")
            phone = input("Enter new phone number (leave blank to keep unchanged): ")
            email = input("Enter new email address (leave blank to keep unchanged): ")
            update_contact(contacts, name, phone, email)
            save_contacts(contacts)
    elif choice=='4':
        name=input("Enter contact name to remove: ")
        if name in contacts:
            del contacts[name]
            print("{} removed from contacts.".format(name))
        else:
            print("{} not found in contacts.".format(name))
    elif choice=='5':
        name=input("Enter contact name to search: ")
        if name in contacts:
            print("{}: {}".format(name, contacts[name]))
        else:
            print("{} not found in contacts".format(name))
    elif choice=='6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number from 1 to 5.")