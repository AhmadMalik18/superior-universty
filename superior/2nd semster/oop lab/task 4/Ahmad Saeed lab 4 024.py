class Book:
    def __init__(self, title, author, publication_year):
        """
        Constructor method to initialize the title, author, and publication_year of the book.
        """
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __str__(self):
        """
        Method to return a string representation of the book in the format:
        "Title: [title], Author: [author], Publication Year: [publication_year]"
        """
        return f"Title: {self.title}, Author: {self.author}, Publication Year: {self.publication_year}"


# Example usage
if __name__ == "__main__":
    # Creating an instance of Book
    book = Book("1984", "George Orwell", 1949)

    # Displaying the book's details using __str__ method
    print(book)
