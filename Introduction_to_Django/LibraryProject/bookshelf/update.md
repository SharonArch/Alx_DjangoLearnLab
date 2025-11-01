```python
from bookshelf.models import Book

# Retrieve the book instance
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Display the updated record
book
Output:

<Book: Nineteen Eighty-Four by George Orwell>
