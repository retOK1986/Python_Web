from mongoengine import Document, StringField, ListField, ReferenceField
from app.models.author import Author

class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author)
    quote = StringField(required=True)