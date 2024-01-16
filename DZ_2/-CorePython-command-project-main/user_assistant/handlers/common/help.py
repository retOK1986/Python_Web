from user_assistant.console.console import Console
from user_assistant.command_enum import CommandEnum

from user_assistant.handlers.abstract_handler import AbstractHandler

column_titles = ['Command', 'Fields', 'Description']

address_book_documentation = [
    [CommandEnum.ADD_CONTACT, 'name, birthday, phone, address, mail', 'Create a new contact'],
    [CommandEnum.EDIT_CONTACT, 'name, birthday, address, mail', 'Edit an existing contact'],
    [CommandEnum.REMOVE_CONTACT, 'name', 'Remove an existing contact'],
    [CommandEnum.FIND_CONTACT, 'name', 'Find a contact by name'],
    [CommandEnum.ADD_PHONE, 'name, phone', 'Add a new phone for contact'],
    [CommandEnum.EDIT_PHONE, 'name', 'Edit an existing phone of contact'],
    [CommandEnum.REMOVE_PHONE, 'name', 'Remove an existing phone of contact'],
    [CommandEnum.SEARCH_CONTACTS, 'name or phone', 'Search contacts by name or phone'],
    [CommandEnum.SHOW_ALL_CONTACTS, '', 'Show all contacts'],
    [CommandEnum.SHOW_BIRTHDAY, 'days', 'Show contacts who birthdays will be in period of entered days'],
]

notes_documentation = [
    [CommandEnum.ADD_NOTE, 'author, text, tag', 'Create a new note'],
    [CommandEnum.EDIT_NOTE, 'id, author, text', 'Edit an existing note'],
    [CommandEnum.REMOVE_NOTE, 'id', 'Remove an existing contact'],
    [CommandEnum.FIND_NOTE, 'id', 'Find a note by id'],
    [CommandEnum.ADD_TAGS, 'id, tags', 'Add tags of note by id'],
    [CommandEnum.REMOVE_TAGS, 'id, tags', 'Remove tags of note by id'],
    [CommandEnum.SHOW_ALL_NOTES, '', 'Show all notes'],
    [CommandEnum.SEARCH_NOTES_BY_TAG, 'tag', 'Search notes by tag'],
    [CommandEnum.SEARCH_NOTES_BY_AUTHOR, 'author', 'Search notes by author'],
    [CommandEnum.SORT_NOTES_BY_TAGS, '', 'Sort notes by tags'],
    [CommandEnum.SORT_NOTES_BY_AUTHOR, '', 'Sort notes by author'],
]

sort_files_documentation = [
    [CommandEnum.SORT_FILES, 'folder', 'Sorting files inside folder by categories: music, image, video, documents'],
]

additional_CommandEnum_documentation = [
    [CommandEnum.EXIT, 'Exit from user assistant'],
    [CommandEnum.CLOSE, 'Exit from user assistant'],
    [CommandEnum.HELP, 'Show documentations'],
]


class HelpHandler(AbstractHandler):
    def execute(self):
        Console.print_table('Address book', column_titles, address_book_documentation)
        Console.print_table('Notes', column_titles, notes_documentation)
        Console.print_table('Sort files', column_titles, sort_files_documentation)
        Console.print_table('Additionals', list(filter(lambda title: title != 'Fields', column_titles)), additional_CommandEnum_documentation)