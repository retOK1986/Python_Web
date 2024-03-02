from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random
from app.models.models import Base, Student, Group, Teacher, Subject, Grade

# Підключення до бази даних
engine = create_engine('postgresql+psycopg2://postgres:123456@localhost/postgres')
Session = sessionmaker(bind=engine)
session = Session()

faker = Faker('uk-UA')

# Створення груп
for _ in range(3):
    group = Group(name=f'{faker.word()} {faker.random_digit()}')
    session.add(group)
session.commit()

# Створення викладачів
for _ in range(3):
    teacher = Teacher(fullname=faker.name())
    session.add(teacher)
session.commit()

# Створення предметів
teachers = session.query(Teacher).all()
for _ in range(5):
    subject = Subject(name=f'{faker.word()} {faker.random_digit()}', teacher=random.choice(teachers))
    session.add(subject)
session.commit()

# Створення студентів і оцінок
groups = session.query(Group).all()
subjects = session.query(Subject).all()
for _ in range(50):  # Створюємо близько 50 студентів
    student = Student(fullname=faker.name(), group=random.choice(groups))
    session.add(student)
    session.commit()  # Зберігаємо студента, щоб отримати ID для зв'язку з оцінками

    for subject in subjects:
        for _ in range(random.randint(1, 20)):  # До 20 оцінок для кожного студента по кожному предмету
            grade = Grade(
                grade=random.randint(1, 12),  # Припустимо, що оцінки від 1 до 12
                grade_date=faker.date_between(start_date='-2y', end_date='today'),
                student_id=student.id,
                subjects_id=subject.id
            )
            session.add(grade)
    session.commit()

print("База даних успішно заповнена випадковими даними.")
