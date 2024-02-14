import psycopg2
from contextlib import contextmanager


@contextmanager
def create_connection():
    try:
        # Створення з'єднання з базою даних
        conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="123456")
        yield conn
    except psycopg2.OperationalError as err:
        # Підняття RuntimeError у випадку помилки з'єднання
        raise RuntimeError(f"Database connection error: {err}")
    finally:
        conn.close()
