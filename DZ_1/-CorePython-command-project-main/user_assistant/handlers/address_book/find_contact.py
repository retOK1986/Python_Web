from user_assistant.address_book.address_book import AddressBook
from user_assistant.class_fields.name import Name
from user_assistant.handlers.input_value import input_value
from user_assistant.console.console import Console
from user_assistant.console.table_format.address_book_table import address_book_titles, get_address_book_row


def find_contact(book: AddressBook):
    Console.print_tip('Press “Enter” with empty value to skip')
    while True:
        name = input_value('contact name', Name, True)

        if not name:
            return
        record = book.find(name.value)

        if record:
            return Console.print_table('Found contact', address_book_titles, [get_address_book_row(record)])
        else:
            return Console.print_error(f'There is no any contact named: {name}')