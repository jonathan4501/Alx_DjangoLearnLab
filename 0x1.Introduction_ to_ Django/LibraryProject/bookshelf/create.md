**Creat a Book instance**
from bookshelf.models import Book

book = Book(title="1984", author="George Orwell", publication_year=1949)
book.objects.create
book.save()

Expected output: Book instance created successfully