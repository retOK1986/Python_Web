from typing import Type

from user_assistant.address_book.address_book import AddressBook
from user_assistant.class_fields.name import Name
from user_assistant.class_fields.phone import Phone
from user_assistant.class_fields.date import Date
from user_assistant.class_fields.address import Address
from user_assistant.class_fields.mail import Mail
from user_assistant.address_book.address_book_record import AddressBookRecord
from user_assistant.storages.storage import Storage
from user_assistant.handlers.input_value import input_value
from user_assistant.console.console import Console
from user_assistant.console.table_format.address_book_table import address_book_titles, get_address_book_row


def add_contact(book: AddressBook, storage: Type[Storage]):
    Console.print_tip('Press “Enter” with empty value to skip')

    while True:
        name = input_value('name', Name, True)

        if not name:
            return

        if book.find(name.value) is not None:
            return Console.print_error(f'Contact {name.value} is already exist')
        else:
            break    
    

    

    date = input_value('date birthday', Date, placeholder=Date.DATE_FORMAT_EXAMPLE)
    mail = input_value('email', Mail, placeholder=Mail.MAIL_FORMAT_EXAMPLE)
    address = input_value('address', Address)
    phone = input_value('phone', Phone, placeholder=Phone.PHONE_FORMAT_EXAMPLE)

    record = AddressBookRecord(name=name, birthday=date, mail=mail, address=address,  phones=[phone])
    book.add(record)
    storage.update(book.data.values())

    Console.print_table('Created contact', address_book_titles, [get_address_book_row(record)])
