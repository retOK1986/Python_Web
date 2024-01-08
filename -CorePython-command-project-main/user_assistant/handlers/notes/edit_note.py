from typing import Type

from user_assistant.class_fields.author import Author
from user_assistant.class_fields.text import Text
from user_assistant.class_fields.id import ID
from user_assistant.notes.notes import Notes
from user_assistant.console.console import Console
from user_assistant.storages.storage import Storage
from user_assistant.handlers.input_value import input_value
from user_assistant.console.table_format.notes_table import note_titles, get_notes_row


NOTES_CLASS = {'author': Author, 'text': Text}

def edit_note(notes: Notes, storage: Type[Storage]):
    Console.print_tip('Press “Enter” with empty value to skip')

    while True:
        value_id = input_value(f'note ID', str)
        
        if value_id:
            existing_note = notes.find(value_id)
            if existing_note:
                break
            else:
                Console.print_error('Input existing ID')
        else:
            return

    for field in NOTES_CLASS:

        if field == 'author':
            volume = str(existing_note.author)
        if field == 'text':  
            volume = str(existing_note.text)  

        new_volume = input_value(f'{field}', NOTES_CLASS[field], True, old_value=volume) 

        if field == 'author' and new_volume:
            existing_note.edit_author(new_volume)

        if field == 'text' and new_volume:
            existing_note.edit_text(new_volume)
                 
    Console.print_table(f'Updated note chahged', note_titles, [get_notes_row(existing_note)])
    storage.update(notes.data.values())