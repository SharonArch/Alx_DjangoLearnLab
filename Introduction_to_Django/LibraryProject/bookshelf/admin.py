from django.contrib import admin
from .models import Book

# Customize how the Book model appears in the admin panel
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to show
    list_filter = ('publication_year',)  # Filter sidebar
    search_fields = ('title', 'author')  # Search bar fields

# Register the Book model and customization
admin.site.register(Book, BookAdmin)
