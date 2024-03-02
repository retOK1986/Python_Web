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

def select_5():
    # Отримуємо список унікальних імен викладачів з бази даних
    teachers = session.query(Teacher.fullname).distinct().all()
    teacher_names = [teacher[0] for teacher in teachers]  # Конвертуємо результати в простий список

    # Виводимо список викладачів з номерами
    print("Виберіть викладача:")
    for index, teacher_name in enumerate(teacher_names, start=1):
        print(f"{index}. {teacher_name}")

    # Запитуємо користувача ввести номер викладача зі списку
    while True:
        try:
            choice = int(input("Введіть номер викладача: ")) - 1
            if 0 <= choice < len(teacher_names):
                selected_teacher = teacher_names[choice]
                break
            else:
                print("Неправильний вибір, спробуйте знову.")
        except ValueError:
            print("Будь ласка, введіть числове значення.")

    # Виконуємо запит до бази даних з обраною назвою викладача
    return session.query(
        Subject.name
    ).join(Teacher).filter(Teacher.fullname == selected_teacher).all()


def select_6():
    # Отримуємо список унікальних назв груп з бази даних
    groups = session.query(Group.name).distinct().all()
    group_names = [group[0] for group in groups]  # Конвертуємо результати в простий список

    # Виводимо список груп з номерами
    print("Виберіть групу:")
    for index, group_name in enumerate(group_names, start=1):
        print(f"{index}. {group_name}")

    # Запитуємо користувача ввести номер групи зі списку
    while True:
        try:
            choice = int(input("Введіть номер групи: ")) - 1
            if 0 <= choice < len(group_names):
                selected_group = group_names[choice]
                break
            else:
                print("Неправильний вибір, спробуйте знову.")
        except ValueError:
            print("Будь ласка, введіть числове значення.")

    # Виконуємо запит до бази даних з обраною назвою групи
    return session.query(
        Student.fullname
    ).join(Group).filter(Group.name == selected_group).all()


def select_7():
    # Отримуємо список унікальних назв груп з бази даних
    groups = session.query(Group.name).distinct().all()
    group_names = [group[0] for group in groups]

    # Виводимо список груп з номерами
    print("Виберіть групу:")
    for index, group_name in enumerate(group_names, start=1):
        print(f"{index}. {group_name}")

    # Запитуємо користувача ввести номер групи зі списку
    while True:
        try:
            group_choice = int(input("Введіть номер групи: ")) - 1
            if 0 <= group_choice < len(group_names):
                selected_group = group_names[group_choice]
                break
            else:
                print("Неправильний вибір, спробуйте знову.")
        except ValueError:
            print("Будь ласка, введіть числове значення.")

    # Отримуємо список унікальних назв предметів з бази даних
    subjects = session.query(Subject.name).distinct().all()
    subject_names = [subject[0] for subject in subjects]

    # Виводимо список предметів з номерами
    print("Виберіть предмет:")
    for index, subject_name in enumerate(subject_names, start=1):
        print(f"{index}. {subject_name}")

    # Запитуємо користувача ввести номер предмету зі списку
    while True:
        try:
            subject_choice = int(input("Введіть номер предмету: ")) - 1
            if 0 <= subject_choice < len(subject_names):
                selected_subject = subject_names[subject_choice]
                break
            else:
                print("Неправильний вибір, спробуйте знову.")
        except ValueError:
            print("Будь ласка, введіть числове значення.")

    # Виконуємо запит до бази даних з обраною групою та предметом
    return session.query(
        Student.fullname,
        Grade.grade
    ).join(Grade, Student.id == Grade.student_id) \
    .join(Subject, Subject.id == Grade.subjects_id) \
    .join(Group, Group.id == Student.group_id) \
    .filter(Group.name == selected_group, Subject.name == selected_subject) \
    .all()



def select_8():
    # Отримуємо список унікальних імен викладачів з бази даних
    teachers = session.query(Teacher.fullname).distinct().all()
    teacher_names = [teacher[0] for teacher in teachers]  # Конвертуємо результати в простий список

    # Виводимо список викладачів з номерами
    print("Виберіть викладача:")
    for index, teacher_name in enumerate(teacher_names, start=1):
        print(f"{index}. {teacher_name}")

    # Запитуємо користувача ввести номер викладача зі списку
    while True:
        try:
            teacher_choice = int(input("Введіть номер викладача: ")) - 1
            if 0 <= teacher_choice < len(teacher_names):
                selected_teacher = teacher_names[teacher_choice]
                break
            else:
                print("Неправильний вибір, спробуйте знову.")
        except ValueError:
            print("Будь ласка, введіть числове значення.")

    # Виконуємо запит до бази даних для отримання середнього балу, який ставить обраний викладач
    return session.query(
        Teacher.fullname,
        func.avg(Grade.grade).label('average_grade')
    ).join(Subject, Teacher.id == Subject.teacher_id) \
    .join(Grade, Subject.id == Grade.subjects_id) \
    .filter(Teacher.fullname == selected_teacher) \
    .group_by(Teacher.fullname).all()

def select_9():
    # Отримуємо список унікальних імен студентів з бази даних
    students = session.query(Student.fullname).distinct().all()
    student_names = [student[0] for student in students]  # Конвертуємо результати в простий список

    # Виводимо список студентів з номерами
    print("Виберіть студента:")
    for index, student_name in enumerate(student_names, start=1):
        print(f"{index}. {student_name}")

    # Запитуємо користувача ввести номер студента зі списку
    while True:
        try:
            student_choice = int(input("Введіть номер студента: ")) - 1
            if 0 <= student_choice < len(student_names):
                selected_student = student_names[student_choice]
                break
            else:
                print("Неправильний вибір, спробуйте знову.")
        except ValueError:
            print("Будь ласка, введіть числове значення.")

    # Виконуємо запит до бази даних для отримання списку предметів, на які записаний обраний студент
    return session.query(
        Subject.name
    ).join(Grade, Subject.id == Grade.subjects_id) \
    .join(Student, Student.id == Grade.student_id) \
    .filter(Student.fullname == selected_student) \
    .group_by(Subject.name).all()

def select_10():
    # Отримуємо список унікальних імен студентів з бази даних
    students = session.query(Student.fullname).distinct().all()
    student_names = [student[0] for student in students]

    # Виводимо список студентів з номерами
    print("Виберіть студента:")
    for index, student_name in enumerate(student_names, start=1):
        print(f"{index}. {student_name}")

    # Запитуємо користувача ввести номер студента зі списку
    while True:
        try:
            student_choice = int(input("Введіть номер студента: ")) - 1
            if 0 <= student_choice < len(student_names):
                selected_student = student_names[student_choice]
                break
            else:
                print("Неправильний вибір, спробуйте знову.")
        except ValueError:
            print("Будь ласка, введіть числове значення.")

    # Отримуємо список унікальних імен викладачів з бази даних
    teachers = session.query(Teacher.fullname).distinct().all()
    teacher_names = [teacher[0] for teacher in teachers]

    # Виводимо список викладачів з номерами
    print("Виберіть викладача:")
    for index, teacher_name in enumerate(teacher_names, start=1):
        print(f"{index}. {teacher_name}")

    # Запитуємо користувача ввести номер викладача зі списку
    while True:
        try:
            teacher_choice = int(input("Введіть номер викладача: ")) - 1
            if 0 <= teacher_choice < len(teacher_names):
                selected_teacher = teacher_names[teacher_choice]
                break
            else:
                print("Неправильний вибір, спробуйте знову.")
        except ValueError:
            print("Будь ласка, введіть числове значення.")

    # Виконуємо запит до бази даних для отримання списку предметів, які викладає обраний викладач для обраного студента
    return session.query(
        Subject.name
    ).join(Grade, Subject.id == Grade.subjects_id) \
    .join(Student, Student.id == Grade.student_id) \
    .join(Teacher, Teacher.id == Subject.teacher_id) \
    .filter(Student.fullname == selected_student, Teacher.fullname == selected_teacher) \
    .group_by(Subject.name).all()

if __name__ == '__main__':
    print(select_10())