from user_assistant.console.console import Console
from user_assistant.console.table_format.address_book_table import address_book_titles, get_address_book_row


def show_all_contacts(book):
    Console.print_table('All contacts', address_book_titles, list(map(get_address_book_row, book.data.values())))