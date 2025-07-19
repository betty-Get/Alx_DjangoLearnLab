from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author_name = "George Orwell"
author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)  # Required by ALX checker
print("Books by George Orwell:")
for book in books:
    print(book.title)

# 2. List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)  # Required by ALX checker
books_in_library = library.books.all()
print("\nBooks in Central Library:")
for book in books_in_library:
    print(book.title)

# 3. Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)  # Required by ALX checker
print(f"\nLibrarian of Central Library: {librarian.name}")
