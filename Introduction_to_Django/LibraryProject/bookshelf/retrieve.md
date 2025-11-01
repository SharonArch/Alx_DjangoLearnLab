
```python
from bookshelf.models import Book

# Retrieve all book records
books = Book.objects.all()
books
Output:

csharp
Copy code
<QuerySet [<Book: 1984 by George Orwell>]>
