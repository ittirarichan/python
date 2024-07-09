contacts={}
print("Customer Detail Book")
while True:
    print("\n1. Add a Contact")
    print("2. Display Contacts")
    print("3. Update contacts" )
    print("4. Remove a Contact")
    print("5. Search for a Contact")
    print("6. Exit\n")
    choice = input("Enter your choice: ")
    if choice=='1':
        name=input("Enter contact name: ")
        number=input("Enter contact number: ")
        email=input("Enter Email id: ")
        place=input("Enter your place: ")
        contacts[name]=number
        print("{} added to contacts.".format(name))
    elif choice=='2':
        if not contacts:
            print("No contacts found.")
        else:
            print("\nContacts:")
            for name, number in contacts.items():
                 print("{:<20}{:<15}{:<30}{:<20}".format(name, number, email, place))
    elif choice == "3":
        name=input('enter your name: ')
        f=0
        for i in contacts:
            if name==i[0]:
                f=1
                name=str(input('enter new name: '))
                number=int(input('enter new number: '))
                email=(input('enter new email: '))
                exp=int(input('enter new place: '))
                i[1]=name
                i[2]=number
                i[3]=email
                i[4]=place
        if f==0:
            print('ivalid id')
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