from user_assistant.notes.notes import Notes
from user_assistant.storages.storage import Storage
from user_assistant.console.console import Console
from user_assistant.class_fields.tag import Tag
from user_assistant.handlers.input_value import input_value
from user_assistant.console.table_format.notes_table import note_titles, get_notes_row

def add_tags(notes: Notes, storage: Storage):
    Console.print_tip('Press “Enter” with empty value to skip')
    while True:
        note_id = input_value('note ID', str, True)
        if not note_id:
            return
        else:
            break
    
    note = notes.find(note_id)

    if note is None:
        Console.print_error(f"No note found with ID {note_id}")
        return

    tags_input = input_value('new tags (separate by comma)', str).strip().casefold()
    new_tags = filter(lambda tag: len(tag) > 0,  tags_input.split(','))
    
    for tag in new_tags:
        note.add_tag(Tag(tag))

    storage.update(notes.data.values())

    # Використання Console.print_table для відображення оновленого запису
    Console.print_table(f'Note updated with new tags', note_titles, [get_notes_row(note)])
