import logging
from psycopg2 import DatabaseError

from connect import create_connection

def create_table(conn, sql_expression: str):
    """Створити таблицю з виразу sql_expression
    :param conn: Об'єкт з'єднання
    :param sql_expression: SQL-вираз для створення таблиці
    :return:
    """
    c = conn.cursor()
    try:
        c.execute(sql_expression)
        conn.commit()
    except DatabaseError as err:
        logging.error(err)
        conn.rollback()
    finally:
        c.close()

if __name__ == '__main__':
    sql_create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
     id SERIAL PRIMARY KEY,
     name VARCHAR(120),
     email VARCHAR(120),
     password VARCHAR(120),
     age SMALLINT CHECK (age > 18 AND age < 75)
    );
    """

    try:
        with create_connection() as conn:
            if conn is not None:
                create_table(conn, sql_create_users_table)
            else:
                print("Помилка! Не вдається створити з'єднання з базою даних.")
    except RuntimeError as err:
        logging.error(err)
