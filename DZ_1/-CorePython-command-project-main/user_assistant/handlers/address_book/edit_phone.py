from user_assistant.class_fields.name import Name
from user_assistant.class_fields.phone import Phone
from user_assistant.handlers.input_value import input_value
from user_assistant.console.console import Console
from user_assistant.console.table_format.address_book_table import address_book_titles, get_address_book_row

from .address_book_abstract import AddressBookAbstract


class AddressBookEditPhoneHandler(AddressBookAbstract):
    def execute(self):
        while True:
            name = input_value('contact name', Name)
            record = self.address_book.find(name.value)
            if record:
                break
            else:
                Console.print_error('Input existing name')

        phone = input_value('phone', Phone, placeholder=Phone.PHONE_FORMAT_EXAMPLE)

        if record.find_phone(phone):
            new_phone = input_value('new phone', Phone, placeholder=Phone.PHONE_FORMAT_EXAMPLE)
            record.edit_phone(str(phone), str(new_phone))
            self.storage.update(self.address_book.data.values())
            Console.print_table('Updated contact phone', address_book_titles, [get_address_book_row(record)])
        else:
            Console.print_error(f'Number {phone} is missing from the contact {name}')   