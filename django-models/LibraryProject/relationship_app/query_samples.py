# relationship_app/query_samples.py
from relationship_app.models import Author, Book, Library, Librarian

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author_name = "George Orwell"
specific_author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=specific_author)
print("Books by George Orwell:")
for book in books_by_author:
    print(book.title)

# 2. List all books in a library
library_name = "Central Library"
# <-- REQUIRED LINE for ALX checker
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print("\nBooks in Central Library:")
for book in books_in_library:
    print(book.title)

# 3. Retrieve the librarian for a library
library = Library.objects.get(name=library_name)  # Reuse same name
librarian = library.librarian
print(f"\nLibrarian of Central Library: {librarian.name}")
