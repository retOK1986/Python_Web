from typing import Type

from user_assistant.notes.note_record import NoteRecord
from user_assistant.class_fields.text import Text
from user_assistant.class_fields.author import Author
from user_assistant.class_fields.tag import Tag
from user_assistant.handlers.input_value import input_value
from user_assistant.notes.notes import Notes
from user_assistant.storages.storage import Storage
from user_assistant.console.console import Console
from user_assistant.console.table_format.notes_table import note_titles, get_notes_row


def add_note(notes: Notes, storage: Type[Storage]):
    Console.print_tip('Press “Enter” with empty value to skip')
    while True:
        author = input_value('author',Author, True)
        if not author:
            return
        else:
            break
    text = input_value('text',Text)
    tag = input_value('tag',Tag)

    note_record = NoteRecord(author=author, text=text, tags=[tag])
    notes.add_note(note_record)
    storage.update(notes.data.values())
    

    Console.print_table(f'Created note', note_titles, [get_notes_row(note_record)])