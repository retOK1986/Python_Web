from user_assistant.console.console import Console
import user_assistant.commands as COMMANDS

column_titles = ['Command', 'Fields', 'Description']

address_book_documentation = [
    [COMMANDS.ADD_CONTACT, 'name, birthday, phone, address, mail', 'Create a new contact'],
    [COMMANDS.EDIT_CONTACT, 'name, birthday, address, mail', 'Edit an existing contact'],
    [COMMANDS.REMOVE_CONTACT, 'name', 'Remove an existing contact'],
    [COMMANDS.FIND_CONTACT, 'name', 'Find a contact by name'],
    [COMMANDS.ADD_PHONE, 'name, phone', 'Add a new phone for contact'],
    [COMMANDS.EDIT_PHONE, 'name', 'Edit an existing phone of contact'],
    [COMMANDS.REMOVE_PHONE, 'name', 'Remove an existing phone of contact'],
    [COMMANDS.SEARCH_CONTACTS, 'name or phone', 'Search contacts by name or phone'],
    [COMMANDS.SHOW_ALL_CONTACTS, '', 'Show all contacts'],
    [COMMANDS.SHOW_BIRTHDAY, 'days', 'Show contacts who birthdays will be in period of entered days'],
]

notes_documentation = [
    [COMMANDS.ADD_NOTE, 'author, text, tag', 'Create a new note'],
    [COMMANDS.EDIT_NOTE, 'id, author, text', 'Edit an existing note'],
    [COMMANDS.REMOVE_NOTE, 'id', 'Remove an existing contact'],
    [COMMANDS.FIND_NOTE, 'id', 'Find a note by id'],
    [COMMANDS.ADD_TAGS, 'id, tags', 'Add tags of note by id'],
    [COMMANDS.REMOVE_TAGS, 'id, tags', 'Remove tags of note by id'],
    [COMMANDS.SHOW_ALL_NOTES, '', 'Show all notes'],
    [COMMANDS.SEARCH_NOTES_BY_TAG, 'tag', 'Search notes by tag'],
    [COMMANDS.SEARCH_NOTES_BY_AUTHOR, 'author', 'Search notes by author'],
    [COMMANDS.SORT_NOTES_BY_TAGS, '', 'Sort notes by tags'],
    [COMMANDS.SORT_NOTES_BY_AUTHOR, '', 'Sort notes by author'],
]

sort_files_documentation = [
    [COMMANDS.SORT_FILES, 'folder', 'Sorting files inside folder by categories: music, image, video, documents'],
]

additional_commands_documentation = [
    [COMMANDS.EXIT, 'Exit from user assistant'],
    [COMMANDS.CLOSE, 'Exit from user assistant'],
    [COMMANDS.HELP, 'Show documentations'],
]
def help():
    Console.print_table('Address book', column_titles, address_book_documentation)
    Console.print_table('Notes', column_titles, notes_documentation)
    Console.print_table('Sort files', column_titles, sort_files_documentation)
    Console.print_table('Additionals', list(filter(lambda title: title != 'Fields', column_titles)), additional_commands_documentation)