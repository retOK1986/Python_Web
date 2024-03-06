from mongoengine import connect

def initialize_db():
    db_name = 'test_retOK'
    db_alias = 'default'
    db_host = 'mongodb+srv://retok1209:vfhrjdtwm@retok.p3bdwlr.mongodb.net/?retryWrites=true&w=majority&appName=retOK'  # URL для підключення

    # Встановлення з'єднання
    connect(db=db_name, alias=db_alias, host=db_host)


# Виклик функції ініціалізації при імпорті цього модуля
initialize_db()