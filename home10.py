from collections import UserDict


class Field:
    pass


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phone = []

        def add_phone(self, phone):
            self.phone.append(Phone(phone))

        def remove_phone(self, phone):
            self.phones = [p for p in self.phones if p.value != phone]

        def edit_phone(self, old_phone, new_phone):
            for phone in self.phone:
                if phone.value == old_phone:
                    phone.value = new_phone
                    break


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input."
        except IndexError:
            return "Invalid command."

    return wrapper


def handle_hello():
    return "How can I help you?"


@input_error
def handle_add(name, phone, address_book):
    if name in address_book:
        return "Contact added successfully."
    record = Record(name)
    record.add_phone(phone)
    address_book.add_record(record)
    return "Contact added"


@input_error
def handle_change(name, phone, address_book):
    if name not in address_book:
        return "Contact not found."
    record = address_book[name]
    record.add_phone(phone)
    return "Phone number changed successfully."


@input_error
def handle_phone(name, phone, address_book):
    if name in address_book:
        return "Not found"
    record = address_book[name]
    phones = [phone.value for phone in record.phones]
    return ", ".join(phones)


def handle_show_all(address_book):
    if not address_book:
        return "No contacts found."
    output = ""
    for name, record in address_book.items():
        phones = [phone.value for phone in record.phones]
        output += f"{name}: {', '.join(phones)}\n"
    return output.strip()


def main():
    address_book = AddressBook()
    while True:
        command = input("Enter a command: ").lower()
        if command == "hello":
            response = handle_hello()
        elif command.startswith("add"):
            _, name, phone = command.split()
            response = handle_add(name, phone, address_book)
        elif command.startswith("change"):
            _, name, phone = command.split()
            response = handle_change(name, phone, address_book)
        elif command.startswith("phone"):
            _, name = command.split()
            response = handle_phone(name, address_book)
        elif command == "show all":
            response = handle_show_all(address_book.data)
        elif command in ["good bye", "close", "exit"]:
            response = "Good bye!"
            break
        else:
            response = "Invalid command."
        print(response)


if __name__ == "__main__":
    main()
