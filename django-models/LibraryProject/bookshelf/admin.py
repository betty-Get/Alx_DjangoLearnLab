from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Show these columns
    list_display = ('title', 'author', 'publication_year')
    # Enable search by title/author
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)
