class Book:
    def __init__(self, title, author, isbn, year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year

    def get_age(self):
        return 2026 - int(self.year)

    def get_summary(self):
        return f"Title: {self.title}, Author: {self.author}, Published: {self.year}"


book1 = Book("Harry Potter and the Philosopher's Stone", "J. K. Rowling", "978-0-7475-3269-9", "1997")
book2 = Book("The Alchemist", "Paulo Coelho", "0-06-250217-4", "1988")
book3 = Book("A Man Called Ove", "Fredrik Backman", "9781476738024", "2012")

print("Book age of Harry Potter:", book1.get_age())
print(book2.get_summary())
print("Release year of A Man Called Ove: ",book3.year)
