from record import Record


def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except Exception as e:
            return f"Error: {e}"
    return wrapper


@input_error
def add_contact(book, args):
    name, phone = args
    record = book.find(name)
    if record:
        record.add_phone(phone)
    else:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
    return "Contact added."


@input_error
def change_phone(book, args):
    name, old, new = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.edit_phone(old, new)
    return "Phone updated."


@input_error
def show_phone(book, args):
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found."
    return ", ".join(p.value for p in record.phones)


def show_all(book):
    if not book.data:
        return "Address book is empty."
    return str(book)
