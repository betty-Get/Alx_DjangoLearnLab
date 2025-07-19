# relationship_app/query_samples.py
from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
specific_author = Author.objects.get(name="George Orwell")
books_by_author = Book.objects.filter(author=specific_author)
print("Books by George Orwell:")
for book in books_by_author:
    print(book.title)

# 2. List all books in a library
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()
print("\nBooks in Central Library:")
for book in books_in_library:
    print(book.title)

# 3. Retrieve the librarian for a library
library = Library.objects.get(name="Central Library")
librarian = library.librarian
print(f"\nLibrarian of Central Library: {librarian.name}")
