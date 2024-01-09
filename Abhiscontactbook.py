import json

def load_contacts():
    try:
        with open("abhicontacts.json", "r") as file:
            contacts = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        contacts = {}
    return contacts

def save_contacts(contacts):
    with open("abhicontacts.json", "w") as file:
        json.dump(contacts, file, indent=2)

def display_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("\n=== Abhi's Contacts ===")
        for name, info in contacts.items():
            print(f"Name: {name}")
            print(f"Mobile: {info['mobile']}")
            print(f"Email: {info['email']}")
            print("------------------")

def add_contact(contacts, name, mobile, email):
    if name in contacts:
        print("Contact already exists. Use update option to modify.")
    else:
        contacts[name] = {"mobile": mobile, "email": email}
        save_contacts(contacts)
        print("Contact added successfully.")

def update_contact(contacts, name, mobile, email):
    if name in contacts:
        contacts[name] = {"mobile": mobile, "email": email}
        save_contacts(contacts)
        print("Contact updated successfully.")
    else:
        print("Contact not found. Use add option to create a new contact.")

def main():
    contacts = load_contacts()

    while True:
        print("\n=== Abhi's Contact Book ===")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. View Contacts")
        print("4. Search Contact")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            name = input("Enter the name: ")
            mobile = input("Enter the mobile number: ")
            email = input("Enter the email address: ")
            add_contact(contacts, name, mobile, email)
        elif choice == "2":
            name = input("Enter the name to update: ")
            mobile = input("Enter the new mobile number: ")
            email = input("Enter the new email address: ")
            update_contact(contacts, name, mobile, email)
        elif choice == "3":
            display_contacts(contacts)
        elif choice == "4":
            name = input("Enter the name to search: ")
            if name in contacts:
                print("\n=== Contact Found ===")
                print(f"Name: {name}")
                print(f"Mobile: {contacts[name]['mobile']}")
                print(f"Email: {contacts[name]['email']}")
                print("------------------")
            else:
                print("Contact not found.")
        elif choice == "5":
            print("Exiting Abhi's Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()
