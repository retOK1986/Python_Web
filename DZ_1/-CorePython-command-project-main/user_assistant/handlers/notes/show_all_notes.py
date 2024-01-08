from user_assistant.console.console import Console
from user_assistant.console.table_format.notes_table import note_titles, get_notes_row


def show_all_notes(notes):
    Console.print_table('All notes', note_titles, list(map(get_notes_row, notes.data.values())))