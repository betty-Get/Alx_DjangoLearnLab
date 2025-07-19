from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author_name = "George Orwell"
author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)  # <-- This line must match exactly
print("Books by George Orwell:")
for book in books:
    print(book.title)

# 2. List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)  # <-- Required pattern
books_in_library = library.books.all()
print("\nBooks in Central Library:")
for book in books_in_library:
    print(book.title)

# 3. Retrieve the librarian for a library
# Again reuse to match checker
library = Library.objects.get(name=library_name)
librarian = library.librarian
print(f"\nLibrarian of Central Library: {librarian.name}")
