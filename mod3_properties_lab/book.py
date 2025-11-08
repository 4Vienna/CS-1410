"""
Complete Lab 4 and update the following information:

Author: [Your Name]
Date: [Date]
"""
class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author

    def __str__(self):
        return f"{self._title} by {self._author}"
    
    def get_title(self):
        return self._title

    def set_title(self, value):
        """Set the title of the book with validation."""
        if not isinstance(value, str):
            raise TypeError("title must be a string")
        if value == "":
            raise ValueError("title cannot be empty")
        self._title = value

    title = property(get_title, set_title)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        """Set the author of the book with validation."""
        if not isinstance(value, str):
            raise TypeError("author must be a string")
        if value == "":
            raise ValueError("author cannot be empty")
        self._author = value

    @property
    def description(self):
        """Read-only description derived from the title and author."""
        return f"{self.title} was written by {self.author}."





def main():
    my_book = Book("Book", "Author")

    my_book.title = "Inkheart"
    my_book.author = "Cornelia Funke"
    print(my_book)

    #my_book.description = f"{my_book.title} is a book written by {my_book.author}"
    print(my_book.description)
if __name__ == "__main__":
    main()