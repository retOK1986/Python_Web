from typing import Type

from user_assistant.address_book.address_book import AddressBook
from user_assistant.class_fields.name import Name
from user_assistant.class_fields.date import Date
from user_assistant.class_fields.address import Address
from user_assistant.class_fields.mail import Mail
from user_assistant.storages.storage import Storage
from user_assistant.handlers.input_value import input_value
from user_assistant.console.console import Console
from user_assistant.console.table_format.address_book_table import address_book_titles, get_address_book_row


FIELDS_CLASS = {'name': (Name, None), 'birthday': (Date, Date.DATE_FORMAT_EXAMPLE), 'email': (Mail, Mail.MAIL_FORMAT_EXAMPLE), 'address': (Address, None)}


def edit_contact(book: AddressBook, storage: Type[Storage]):
    Console.print_tip('Press “Enter” with empty value to skip')

    while True:

        name = Console.input('Enter contact name: ')

        if not name:
            return

        record = book.find(name)

        if record is None:
            Console.print_error('Input existing name')
        else:
            break    
     
    for field in FIELDS_CLASS.keys():
            if field ==  'name':
                old_value = str(record.name)
            elif field == 'birthday':
                old_value = str(record.birthday)
            elif field == 'email':
                old_value = str(record.mail)
            elif field == 'address':
                old_value = str(record.address)       

            field_class, placeholder = FIELDS_CLASS[field]
            volume = input_value(f'{field}', field_class, True, old_value=old_value, placeholder=placeholder)
            
            if field == 'birthday' and volume:
                record.edit_birthday(volume)
            elif field == 'email' and volume:
                record.edit_email(volume)
            elif field == 'address' and volume:
                record.edit_address(volume)
            elif field == 'name' and volume:
                book.delete(str(record.name))
                record.edit_name(volume)
                book.add(record)
            
    storage.update(book.data.values())

    Console.print_table('Updated contact', address_book_titles, [get_address_book_row(record)])
