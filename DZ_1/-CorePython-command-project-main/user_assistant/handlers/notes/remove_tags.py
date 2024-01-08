from user_assistant.notes.notes import Notes
from user_assistant.storages.storage import Storage
from user_assistant.console.console import Console
from user_assistant.class_fields.tag import Tag
from user_assistant.handlers.input_value import input_value
from user_assistant.console.table_format.notes_table import note_titles, get_notes_row

def remove_tags(notes: Notes, storage: Storage):
    note_id = input_value('note ID', str)
    note = notes.find(note_id)

    if note is None:
        Console.print_error(f"No note found with ID {note_id}")
        return
    
    Console.print_table(f'Note updated with removed tags', note_titles, [get_notes_row(note)])
    while True:
        tags_input = input_value('selected tags to remove (separate by comma)', str, True).strip().casefold()
        
        if tags_input:
            tags_to_remove = set(filter(lambda tag: len(tag) > 0,  tags_input.split(',')))
            
            if  set(note.str_tags).isdisjoint(tags_to_remove):
                Console.print_error(f'Tag missing in tags')
                break
            else:
                for tag in tags_to_remove:
                    if tag in note.tags:
                        note.remove_tag(tag)
                storage.update(notes.data.values())
                return Console.print_table(f'Note updated with removed tags', note_titles, [get_notes_row(note)])

        else:
            break

    
