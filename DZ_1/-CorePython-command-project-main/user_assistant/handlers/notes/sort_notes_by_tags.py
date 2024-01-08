from user_assistant.console.console import Console
from user_assistant.console.table_format.notes_table import note_titles, get_notes_row
from user_assistant.notes.notes import Notes

def sort_notes_by_tags(notes: Notes):
    result_sort = notes.sort_by_tags()
    
    Console.print_table(f'Sorted notes by tag: ', note_titles, list(map(get_notes_row,result_sort)))

    
     