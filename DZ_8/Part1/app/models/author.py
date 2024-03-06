from mongoengine import Document, StringField, connect

# Підключення до MongoDB
connect('test_retok', host='mongodb+srv://retok1209:vfhrjdtwm@retok.p3bdwlr.mongodb.net/?retryWrites=true&w=majority&appName=retOK')

class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField(required=True)
    born_location = StringField(required=True)
    description = StringField(required=True)