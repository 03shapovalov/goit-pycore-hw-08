import pickle

class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone
        print(f"Added contact: {name} - {phone}")

    def get_contact(self, name):
        contact = self.contacts.get(name)
        if contact:
            print(f"Contact: {name} - {contact}")
        else:
            print("Contact not found.")
        return contact

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Deleted contact: {name}")
        else:
            print("Contact not found.")

    def list_contacts(self):
        if self.contacts:
            for name, phone in self.contacts.items():
                print(f"{name}: {phone}")
        else:
            print("No contacts found.")

    def save_data(self, filename="addressbook.pkl"):
        with open(filename, "wb") as f:
            pickle.dump(self, f)
        print("Address book saved.")

    @staticmethod
    def load_data(filename="addressbook.pkl"):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            print("No address book found. Creating a new one.")
            return AddressBook()

def main():
    address_book = AddressBook.load_data()

    while True:
        command = input("Enter command (add, get, delete, list, exit): ").strip().lower()
        if command == "add":
            name = input("Enter name: ").strip()
            phone = input("Enter phone: ").strip()
            address_book.add_contact(name, phone)
        elif command == "get":
            name = input("Enter name: ").strip()
            address_book.get_contact(name)
        elif command == "delete":
            name = input("Enter name: ").strip()
            address_book.delete_contact(name)
        elif command == "list":
            address_book.list_contacts()
        elif command == "exit":
            address_book.save_data()
            break
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
