from typing import Type

from user_assistant.address_book.address_book import AddressBook
from user_assistant.class_fields.name import Name
from user_assistant.class_fields.phone import Phone
from user_assistant.storages.storage import Storage
from user_assistant.handlers.input_value import input_value
from user_assistant.console.console import Console
from user_assistant.console.table_format.address_book_table import address_book_titles, get_address_book_row

def remove_phone(book: AddressBook, storage: Type[Storage]):
    Console.print_tip('Press “Enter” with empty value to skip')
    while True:
        name = input_value('contact name', Name, True)
        if not name:
            return
        record = book.find(name.value)
        if record:
            break
        else:
            Console.print_error('Input existing name')
            
    Console.print_table('Select contact phone', address_book_titles, [get_address_book_row(record)])
    phone = input_value('phone', Phone, placeholder=Phone.PHONE_FORMAT_EXAMPLE)

    if record.find_phone(phone):
        record.remove_phone(phone)
        storage.update(book.data.values()) 
        Console.print_table('Updated contact phone', address_book_titles, [get_address_book_row(record)])
    else:
        Console.print_error(f'Number {phone} is missing from the contact {name}')