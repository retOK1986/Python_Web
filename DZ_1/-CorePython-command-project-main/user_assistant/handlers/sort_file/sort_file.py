from pathlib import Path
from user_assistant.sort_file.file_sorter import FileSorter
from user_assistant.console.console import Console


def sort_files():
    try:
        folder_for_scan = Console.input('Enter folder for scan: ')
        sorter = FileSorter(Path(folder_for_scan))
        sorter.sort_files()

        Console.print_error('The directory was sorted.')
    except (FileNotFoundError, OSError) as e:
        Console.print_error(f'Error: {e}')