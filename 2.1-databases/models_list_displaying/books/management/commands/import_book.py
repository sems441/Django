from django.core.management.base import BaseCommand
from books.models import Book
import json


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('fixtures/books.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        for item in data:
            name = item.get('fields').get('name')
            author = item.get('fields').get('author')
            pub_date = item.get('fields').get('pub_date')
            book = Book.objects.create(name=name, author=author, pub_date=pub_date)
            book.save()
