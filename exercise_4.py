def main():
    contacts = {}

    while True:
        command_input = input("Enter a command: ").strip().lower()

        if command_input in ['exit', 'close']:
            print("Exiting program...")
            break
        elif command_input == 'hello':
            print("How can I help you?")
        else:
            command, args = parse_input(command_input)

            if command == 'add':
                if len(args) != 2:
                    print("Invalid command format. Use: add [name] [phone number]")
                else:
                    add_contact(contacts, args[0], args[1])
            elif command == 'change':
                if len(args) != 2:
                    print("Invalid command format. Use: change [name] [new phone number]")
                else:
                    change_contact(contacts, args[0], args[1])
            elif command == 'phone':
                if len(args) != 1:
                    print("Invalid command format. Use: phone [name]")
                else:
                    show_phone(contacts, args[0])
            elif command == 'all':
                show_all_contacts(contacts)
            else:
                print("Invalid command. Please try again.")


def parse_input(command_input):
    parts = command_input.split()
    command = parts[0]
    args = parts[1:]  # залишаємо всі аргументи після команди
    return command, args


def add_contact(contacts, name, phone_number):
    contacts[name] = phone_number
    print(f"Contact '{name}' added.")


def change_contact(contacts, name, new_phone_number):
    if name in contacts:
        contacts[name] = new_phone_number
        print(f"Phone number for '{name}' updated.")
    else:
        print(f"Contact '{name}' not found.")


def show_phone(contacts, name):
    if name in contacts:
        phone_number = contacts[name]
        print(f"Phone number for '{name}' is {phone_number}.")
    else:
        print(f"Contact '{name}' not found.")


def show_all_contacts(contacts):
    if contacts:
        print("List of contacts:")
        for name, phone_number in contacts.items():
            print(f"{name}: {phone_number}")
    else:
        print("No contacts saved.")


if __name__ == "__main__":
    print("Welcome to the assistant bot!")
    main()
