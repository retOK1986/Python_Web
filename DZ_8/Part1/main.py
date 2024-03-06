from Part1.app.models.author import Author
from Part1.app.models.quote import Quote
from Part1.app.utils.loader import load_authors, load_quotes
from mongoengine import connect, disconnect
import redis
import json

# Від'єднати існуюче підключення, якщо воно існує
disconnect()
# Налаштування підключення до MongoDB
connect('test_retOK', host='mongodb+srv://retok1209:vfhrjdtwm@retok.p3bdwlr.mongodb.net/?retryWrites=true&w=majority&appName=retOK')

# Налаштування підключення до Redis
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def cache_search_results(key, results):
    """Кешування результатів пошуку у Redis."""
    redis_client.set(key, json.dumps(results), ex=3600)  # Кешувати результат на 1 годину

def search_quotes(command, value):
    """Пошук цитат за командою та значенням."""
    cache_key = f"{command}:{value}"
    cached_results = redis_client.get(cache_key)

    if cached_results:
        return json.loads(cached_results)

    results = []
    if command == "name":
        author = Author.objects(fullname__icontains=value).first()
        if author:
            quotes = Quote.objects(author=author).all()
            results = [quote.quote for quote in quotes]
    elif command == "tag":
        quotes = Quote.objects(tags=value).all()
        results = [quote.quote for quote in quotes]
    elif command == "tags":
        tags = value.split(",")
        quotes = Quote.objects(tags__in=tags).all()
        results = [quote.quote for quote in quotes]

    cache_search_results(cache_key, results)
    return results

def main():
    # Завантаження даних з JSON файлів
    load_authors('data/authors.json')
    load_quotes('data/quotes.json')

    while True:
        command = input("Enter command (or 'exit' to quit): ")
        if command == "exit":
            break

        try:
            cmd, value = command.split(":", 1)
            value = value.strip()
            results = search_quotes(cmd, value)
            if results:
                for quote in results:
                    print(quote)
            else:
                print("No results found.")
        except ValueError:
            print("Invalid command format. Please use 'name:value', 'tag:value', or 'tags:value1,value2,...'")

if __name__ == "__main__":
    main()