from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from app.models.models import Student, Group, Teacher, Subject, Grade

engine = create_engine('postgresql+psycopg2://postgres:123456@localhost/postgres')
Session = sessionmaker(bind=engine)
session = Session()
def select_1():
    # Знайти 5 студентів із найбільшим середнім балом з усіх предметів
    return session.query(
        Student.fullname,
        func.avg(Grade.grade).label('average_grade')
    ).join(Grade).group_by(Student.id).order_by(func.avg(Grade.grade).desc()).limit(5).all()


def select_2():
    # Запитуємо користувача ввести назву предмету
    subject_name = input("Будь ласка, введіть назву предмету: ")

    # Виконуємо запит до бази даних з використанням введеної назви предмету
    return session.query(
        Student.fullname,
        func.avg(Grade.grade).label('average_grade')
    ).join(Grade).join(Subject).filter(Subject.name == subject_name).group_by(Student.id).order_by(
        func.avg(Grade.grade).desc()).first()


def select_3():
    # Запитуємо користувача ввести назву групи
    group_name = input("Будь ласка, введіть назву групи: ")

    # Запитуємо користувача ввести назву предмету
    subject_name = input("Будь ласка, введіть назву предмету: ")

    # Виконуємо запит до бази даних з використанням введених назв групи та предмету
    return session.query(
        Group.name,
        func.avg(Grade.grade).label('average_grade')
    ).select_from(Group) \
    .join(Student, Group.id == Student.group_id) \
    .join(Grade, Student.id == Grade.student_id) \
    .join(Subject, Subject.id == Grade.subjects_id) \
    .filter(Group.name == group_name, Subject.name == subject_name) \
    .group_by(Group.id).all()

def select_4():
    # Знайти середній бал на потоці (по всій таблиці оцінок)
    return session.query(func.avg(Grade.grade).label('average_grade')).scalar()

def select_5(teacher_name):
    # Знайти які курси читає певний викладач
    return session.query(
        Subject.name
    ).join(Teacher).filter(Teacher.fullname == teacher_name).all()

def select_6(group_name):
    # Знайти список студентів у певній групі
    return session.query(
        Student.fullname
    ).join(Group).filter(Group.name == group_name).all()

def select_7(group_name, subject_name):
    # Знайти оцінки студентів у окремій групі з певного предмета
    return session.query(
        Student.fullname,
        Grade.grade
    ).join(Group).join(Grade).join(Subject).filter(Group.name == group_name, Subject.name == subject_name).all()

def select_8(teacher_name):
    # Знайти середній бал, який ставить певний викладач зі своїх предметів
    return session.query(
        func.avg(Grade.grade).label('average_grade')
    ).join(Subject).join(Teacher).filter(Teacher.fullname == teacher_name).scalar()

def select_9(student_name):
    # Знайти список курсів, які відвідує певний студент
    return session.query(
        Subject.name
    ).join(Grade).join(Student).filter(Student.fullname == student_name).group_by(Subject.id).all()

def select_10(student_name, teacher_name):
    # Список курсів, які певному студенту читає певний викладач
    return session.query(
        Subject.name
    ).join(Teacher).join(Grade).join(Student).filter(Student.fullname == student_name, Teacher.fullname == teacher_name).group_by(Subject.id).all()

