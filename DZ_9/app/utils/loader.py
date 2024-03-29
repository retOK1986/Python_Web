import json
from mongoengine import connect, disconnect, DoesNotExist
from app.models.author import Author
from app.models.quote import Quote
import os

disconnect()

# Підключення до MongoDB
connect('test_retOK', alias='default', host='mongodb+srv://retok1209:vfhrjdtwm@retok.p3bdwlr.mongodb.net/?retryWrites=true&w=majority&appName=retOK')

def load_authors(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        authors_list = json.load(f)
        for author_data in authors_list:
            try:
                # Перевірка чи автор вже існує
                Author.objects.get(fullname=author_data['fullname'])
            except DoesNotExist:
                # Створення нового автора, якщо він не існує
                Author(**author_data).save()
    print(f"Loaded authors from {file_path}")

def load_quotes(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        quotes_list = json.load(f)
        for quote_data in quotes_list:
            author_name = quote_data.pop('author', None)
            author = Author.objects(fullname=author_name).first()
            if author:
                # Перевірка чи цитата вже існує
                if not Quote.objects(quote=quote_data.get('quote')):
                    Quote(author=author, **quote_data).save()
            else:
                print(f"Author not found for quote: {quote_data.get('quote', 'Unknown')}")
    print(f"Loaded quotes from {file_path}")

def main():
    base_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
    authors_file_path = os.path.join(base_path, 'authors.json')
    quotes_file_path = os.path.join(base_path, 'quotes.json')
    load_authors(authors_file_path)
    load_quotes(quotes_file_path)

if __name__ == '__main__':
    main()
