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


book1 = Book("Attack on Titan", "Isayama", "123456", "2020")
book2 = Book("One Piece", "Eicheiro Oda", "456789", "2002")

print("Book age:", book1.get_age())
print(book2.get_summary())
