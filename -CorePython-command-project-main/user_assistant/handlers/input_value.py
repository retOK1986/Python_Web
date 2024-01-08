from user_assistant.console.console import Console
import keyboard
import pyperclip

def write(old_value, field):
    print(f'Change value {field} :', end='')
    pyperclip.copy(old_value) 
    keyboard.press('ctrl+v') 
    keyboard.release('ctrl+v')
    result = input()
    pyperclip.copy('')
    return result


def input_value(value: str, class_field: classmethod, is_edit=False, old_value = None, placeholder=None):
    while True:
        if old_value:
            result = write(old_value, str(class_field.__name__).casefold())
              
        else:    
            result = Console.input(f'Enter {value}: ', placeholder=placeholder).strip()
        if result == '' and is_edit:
            return result
        try:
            result = class_field(result)
            return result
        except Exception as error:
            Console.print_error(error)
            continue
