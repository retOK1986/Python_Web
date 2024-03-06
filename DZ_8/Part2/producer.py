from mongoengine import connect
from models import Contact
from faker import Faker
import pika
import json

# Підключення до MongoDB
connect(host='mongodb+srv://retok1209:vfhrjdtwm@retok.p3bdwlr.mongodb.net/?retryWrites=true&w=majority&appName=retOK')

# Підключення до RabbitMQ
parameters = pika.URLParameters('amqps://jhaaqjxk:aQtyNTra5fO4KeB2vc26pX4DIG8ZbVlP@sparrow.rmq.cloudamqp.com/jhaaqjxk')  # Ваш URL для підключення до RabbitMQ
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='emails')

def create_contacts_and_send_messages(n):
    # Генерація фейкових контактів
    fake = Faker()
    for _ in range(n):  # Генерувати n контактів
        full_name = fake.name()
        email = fake.email()
        contact = Contact(full_name=full_name, email=email)
        contact.save()

        # Відправлення ObjectID контакту у чергу RabbitMQ
        message = json.dumps({'contact_id': str(contact.id)})
        channel.basic_publish(exchange='',
                              routing_key='emails',
                              body=message)
        print(f"Sent message for contact ID: {contact.id}")

    connection.close()

# Генерація та відправлення 10 контактних повідомлень
create_contacts_and_send_messages(10)
