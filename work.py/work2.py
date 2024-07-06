
contacts = {}

print("Simple Contact List")

while True:
    print("\n1. Display Contacts")
    print("2. Add a Contact")
    print("3. Remove a Contact")
    print("4. Search for a Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        if not contacts:
            print("No contacts found.")
        else:
            print("Contacts:")
            for name, number in contacts.items():
                print(f"{name}: {number}")
    elif choice == '2':
        name = input("Enter contact name: ")
        number = input("Enter contact number: ")
        contacts[name] = number
        print(f"{name} added to contacts.")
    elif choice == '3':
        name = input("Enter contact name to remove: ")
        if name in contacts:
            del contacts[name]
            print(f"{name} removed from contacts.")
        else:
            print(f"{name} not found in contacts.")
    elif choice == '4':
        name = input("Enter contact name to search: ")
        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print(f"{name} not found in contacts.")
    elif choice == '5':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")

