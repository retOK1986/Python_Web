import logging
import random
from faker import Faker
import sqlite3

fake = Faker()

# Підключення до бази даних SQLite
conn = sqlite3.connect('example.db')  # це створить файл example.db в поточній директорії
cur = conn.cursor()

# Створення таблиць, якщо вони ще не існують (приклад)
cur.execute('''CREATE TABLE IF NOT EXISTS groups (id INTEGER PRIMARY KEY, name TEXT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS teachers (id INTEGER PRIMARY KEY, fullname TEXT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS subjects (id INTEGER PRIMARY KEY, name TEXT, teacher_id INTEGER)''')
cur.execute('''CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, fullname TEXT, group_id INTEGER)''')
cur.execute('''CREATE TABLE IF NOT EXISTS grades (id INTEGER PRIMARY KEY, student_id INTEGER, subject_id INTEGER, grade INTEGER, grade_date TEXT)''')

try:
    # Додавання груп
    for _ in range(3):
        cur.execute("INSERT INTO groups (name) VALUES (?)", (fake.word(),))

    # Додавання викладачів
    for _ in range(3):
        cur.execute("INSERT INTO teachers (fullname) VALUES (?)", (fake.name(),))

    # Додавання предметів із вказівкою викладача
    for teacher_id in range(1, 4):
        for _ in range(2):
            cur.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", (fake.word(), teacher_id))

    # Додавання студентів і оцінок
    for group_id in range(1, 4):
        for _ in range(10):
            cur.execute("INSERT INTO students (fullname, group_id) VALUES (?, ?)", (fake.name(), group_id))
            student_id = cur.lastrowid
            for subject_id in range(1, 7):
                for _ in range(3):
                    cur.execute("INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (?, ?, ?, ?)",
                                (student_id, subject_id, random.randint(0, 100), fake.date_this_decade()))

    conn.commit()  # Збереження змін
except sqlite3.DatabaseError as e:
    logging.error(e)
    conn.rollback()  # Ролбек у разі помилки
finally:
    cur.close()
    conn.close()  # Закриття підключення
