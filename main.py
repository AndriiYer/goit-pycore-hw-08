from data import load_data, save_data
from bot import add_contact, change_phone, show_phone, show_all

def main():
    book = load_data()

    print("AddressBook Bot. Type 'help' for commands.")

    while True:
        command = input(">>> ").strip().lower()

        if command in ("exit", "close", "good bye"):
            save_data(book)
            print("Data saved. Bye!")
            break

        if command.startswith("add "):
            _, name, phone = command.split()
            print(add_contact(book, (name, phone)))
            continue

        if command.startswith("change "):
            _, name, old, new = command.split()
            print(change_phone(book, (name, old, new)))
            continue

        if command.startswith("phone "):
            _, name = command.split()
            print(show_phone(book, (name,)))
            continue

        if command == "all":
            print(show_all(book))
            continue

        if command == "help":
            print("""
Commands:
  add <name> <phone>
  change <name> <old> <new>
  phone <name>
  all
  exit
""")
            continue

        print("Unknown command. Type 'help'.")


if __name__ == "__main__":
    main()
