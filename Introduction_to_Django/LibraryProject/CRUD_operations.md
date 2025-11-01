🟩 Create
from bookshelf.models import Book

# Create a new book record
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book


Output:

<Book: 1984 by George Orwell>


🟦 Retrieve
from bookshelf.models import Book

# Retrieve all book records
books = Book.objects.all()
books


Output:

<QuerySet [<Book: 1984 by George Orwell>]>


🟨 Update
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


🟥 Delete
from bookshelf.models import Book

# Retrieve and delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Check all remaining books
Book.objects.all()


Output:

(1, {'bookshelf.Book': 1})
<QuerySet []>
