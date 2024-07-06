

def add_contact(contacts, name, phone, email):
    contacts[name] = {'phone': phone, 'email': email}

def search_contact(contacts, name):
    return contacts.get(name)

def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print(f"Contact '{name}' not found.")

def update_contact(contacts, name, phone, email):
    if name in contacts:
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        print(f"Contact '{name}' updated.")
    else:
        print(f"Contact '{name}' not found.")

def view_all_contacts(contacts):
    if contacts:
        print("\nAll Contacts:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("\nNo contacts found.")

def main():
    contacts = load_contacts()

    while True:
        print("\nContact Book Menu:\n")
        print("1. Add a Contact")
        print("2. Search for a Contact")
        print("3. Delete a Contact")
        print("4. Update Contact Information")
        print("5. View All Contacts")
        print("6. Exit ")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            add_contact(contacts, name, phone, email)
            save_contacts(contacts)

        elif choice == "2":
            name = input("Enter name to search: ")
            contact = search_contact(contacts, name)
            if contact:
                print(f"Name: {name}, Phone: {contact['phone']}, Email: {contact['email']}")
            else:
                print("Contact not found.")

        elif choice == "3":
            name = input("Enter name to delete: ")
            delete_contact(contacts, name)
            save_contacts(contacts)

        elif choice == "4":
            name = input("Enter name to update: ")
            phone = input("Enter new phone number (leave blank to keep unchanged): ")
            email = input("Enter new email address (leave blank to keep unchanged): ")
            update_contact(contacts, name, phone, email)
            save_contacts(contacts)

        elif choice == "5":
            view_all_contacts(contacts)

        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
