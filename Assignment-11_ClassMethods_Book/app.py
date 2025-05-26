class Book:
    total_books = 0 # Class variable to keep track of total books

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
    
    @classmethod
    def display_total_books(cls):
        print(f"Total books added: {cls.total_books}")

# Creating book instances
book1 = Book("Python Basics")
book2 = Book("OOP Concepts")
book3 = Book("Data Structures")

# Display total number of books
Book.display_total_books()


    