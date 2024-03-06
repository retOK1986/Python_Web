from mongoengine import Document, StringField, ListField, ReferenceField
from Part1.app.models.author import Author

class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author)
    quote = StringField(required=True)