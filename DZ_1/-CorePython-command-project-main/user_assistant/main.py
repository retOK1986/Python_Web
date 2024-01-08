from pathlib import Path

from . import commands as COMMANDS
from .handlers.address_book.add_contact import add_contact
from .handlers.address_book.remove_contact import remove_contact
from .handlers.address_book.edit_contact import edit_contact
from .handlers.address_book.find_contact import find_contact
from .handlers.address_book.show_birthday import show_birthday
from .handlers.address_book.show_all_contacts import show_all_contacts
from .handlers.address_book.search_contact import search_contacts
from .handlers.address_book.add_phone import add_phone
from .handlers.address_book.edit_phone import edit_phone
from .handlers.address_book.remove_phone import remove_phone
from .handlers.sort_file.sort_file import sort_files
from .handlers.do_exit import do_exit

from .address_book.address_book import AddressBook
from .storages.csv_storage import CSVStorage
from .serializers.address_book.address_book_csv_serializer import AddressBookCSVSerializer

from .notes.notes import Notes
from .serializers.notes.notes_csv_serializer import NotesCSVSerializer
from .handlers.notes.add_note import add_note
from .handlers.notes.find_note import find_note
from .handlers.notes.remove_note import remove_note
from .handlers.notes.search_notes_by_author import search_notes_by_author
from .handlers.notes.search_notes_by_tag import search_notes_by_tag
from .handlers.notes.edit_note import edit_note
from .handlers.notes.sort_notes_by_tags import sort_notes_by_tags
from .handlers.notes.sort_notes_by_author import sort_notes_by_author
from .handlers.notes.remove_tags import remove_tags
from .handlers.notes.add_tags import add_tags
from .handlers.greeting import greeting
from .handlers.notes.show_all_notes import show_all_notes
from .handlers.help import help

from .console.console import Console

STORAGE_PATH = Path('.') / Path('databases')

ADDRESS_BOOK_FIELDS = ['name', 'birthday', 'address', 'phones', 'mail', 'updated_at', 'created_at']
NOTE_FIELDS = ['author', 'text', 'tags', 'id', 'updated_at', 'created_at']

address_book_storage = CSVStorage(STORAGE_PATH, 'address_book.csv', AddressBookCSVSerializer, ADDRESS_BOOK_FIELDS)
book = AddressBook(address_book_storage.get())

notes_storage = CSVStorage(STORAGE_PATH, 'notes.csv', NotesCSVSerializer, NOTE_FIELDS)
notes = Notes(notes_storage.get())

prompts = list(map(lambda name: getattr(COMMANDS, name), filter(lambda name: not name.startswith('__'), dir(COMMANDS))))


def main():
    greeting()

    while True:

        user_input = Console.input('Enter command: ', prompts).casefold().strip()

        if user_input == COMMANDS.ADD_CONTACT:
            add_contact(book, address_book_storage)
            continue

        if user_input == COMMANDS.REMOVE_CONTACT:
            remove_contact(book, address_book_storage)
            continue

        if user_input == COMMANDS.EDIT_CONTACT:
            edit_contact(book, address_book_storage)
            continue

        if user_input == COMMANDS.FIND_CONTACT:
            find_contact(book)
            continue

        if user_input == COMMANDS.SHOW_BIRTHDAY:
            show_birthday(book)
            continue

        if user_input == COMMANDS.SHOW_ALL_CONTACTS:
            show_all_contacts(book)
            continue

        if user_input == COMMANDS.SEARCH_CONTACTS:
            search_contacts(book)
            continue

        if user_input == COMMANDS.ADD_PHONE:
            add_phone(book, address_book_storage)
            continue

        if user_input == COMMANDS.EDIT_PHONE:
            edit_phone(book, address_book_storage)
            continue

        if user_input == COMMANDS.REMOVE_PHONE:
            remove_phone(book, address_book_storage)
            continue

        if user_input == COMMANDS.SORT_FILES:
            sort_files()
            continue

        if user_input in (COMMANDS.EXIT, COMMANDS.CLOSE):
            do_exit()
            break

        if user_input == COMMANDS.ADD_NOTE:
            add_note(notes, notes_storage)
            continue

        if user_input == COMMANDS.FIND_NOTE:
            find_note(notes)
            continue

        if user_input == COMMANDS.SHOW_ALL_NOTES:
            show_all_notes(notes)
            continue

        if user_input == COMMANDS.REMOVE_NOTE:
            remove_note(notes, notes_storage)
            continue

        if user_input == COMMANDS.SEARCH_NOTES_BY_TAG:
            search_notes_by_tag(notes)
            continue

        if user_input == COMMANDS.SEARCH_NOTES_BY_AUTHOR:
            search_notes_by_author(notes)
            continue

        if user_input == COMMANDS.EDIT_NOTE:
            edit_note(notes, notes_storage)
            continue

        if user_input == COMMANDS.SORT_NOTES_BY_TAGS:
            sort_notes_by_tags(notes)
            continue

        if user_input == COMMANDS.SORT_NOTES_BY_AUTHOR:
            sort_notes_by_author(notes)
            continue

        if user_input == COMMANDS.REMOVE_TAGS:
            remove_tags(notes, notes_storage)
            continue

        if user_input == COMMANDS.ADD_TAGS:
            add_tags(notes, notes_storage)
            continue

        if user_input == COMMANDS.HELP:
            help()
            continue

        Console.print_tip('Enter [bold deep_sky_blue1]help[/] to see all possible commands')
