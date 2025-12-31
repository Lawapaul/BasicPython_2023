class Book:
    def __init__(self,title,author,isbn,is_available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    def __str__(self):
        return f"{self.title},{self.author},{self.isbn},{self.is_available}\n"

class Member:
    def __init__(self,member_id,name,borrowed_books_isbns):
        self.member_id = member_id
        self.name = name
        self.borrowed_books_isbns = borrowed_books_isbns

    def __str__(self):
        return f"{self.member_id},{self.name},{self.borrowed_books_isbns}"