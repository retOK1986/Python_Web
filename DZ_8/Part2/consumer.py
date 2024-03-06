from mongoengine import connect
from models import Contact
import pika
import json
import os

# Підключення до MongoDB
connect(host='mongodb+srv://retok1209:vfhrjdtwm@retok.p3bdwlr.mongodb.net/?retryWrites=true&w=majority&appName=retOK')

# Підключення до RabbitMQ
parameters = pika.URLParameters('amqps://jhaaqjxk:aQtyNTra5fO4KeB2vc26pX4DIG8ZbVlP@sparrow.rmq.cloudamqp.com/jhaaqjxk')  # Ваш URL для підключення до RabbitMQ
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='emails')

def callback(ch, method, properties, body):
    data = json.loads(body)
    contact_id = data['contact_id']

    # Імітація відправки email
    print(f"Sending email to contact ID: {contact_id}")
    # Тут може бути ваш код для відправлення email

    # Оновлення статусу контакту в базі даних
    contact = Contact.objects(id=contact_id).first()
    if contact:
        contact.message_sent = True
        contact.save()
        print(f"Message sent to {contact.full_name}")

channel.basic_consume(queue='emails',
                      auto_ack=True,
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
