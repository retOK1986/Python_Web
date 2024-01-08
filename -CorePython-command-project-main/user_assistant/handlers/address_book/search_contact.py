from user_assistant.console.console import Console
from user_assistant.console.table_format.address_book_table import address_book_titles, get_address_book_row


def search_contacts(book):
    while True:
        string = Console.input(f'Input contact name or phone: ')
        if string:
            break
        Console.print_error('Value is empty. Please try again')

    records = book.search(string)

    Console.print_table('Searched contacts', address_book_titles, list(map(get_address_book_row, records)))