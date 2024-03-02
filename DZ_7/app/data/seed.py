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
    group = Group(name=faker.word())
    session.add(group)
session.commit()

# Створення викладачів
teachers = []
for _ in range(3):
    teacher = Teacher(fullname=faker.name())
    session.add(teacher)
    teachers.append(teacher)
session.commit()

# Створення предметів
subjects = []
for _ in range(5):
    subject = Subject(name=faker.word(), teacher=random.choice(teachers))
    session.add(subject)
    subjects.append(subject)
session.commit()

# Створення студентів і оцінок
groups = session.query(Group).all()
for _ in range(50):
    student = Student(fullname=faker.name(), group=random.choice(groups))
    session.add(student)
    session.commit()  # Зберігаємо студента, щоб отримати ID для зв'язку з оцінками

    for subject in subjects:
        for _ in range(random.randint(5, 20)):  # Кількість оцінок для кожного студента по предмету
            grade = Grade(
                student_id=student.id,
                subject_id=subject.id,
                grade=random.randint(1, 12),  # Припустимо, що оцінки від 1 до 12
                date_received=faker.date_between(start_date='-2y', end_date='today')
            )
            session.add(grade)
session.commit()

print("База даних успішно заповнена випадковими даними.")
