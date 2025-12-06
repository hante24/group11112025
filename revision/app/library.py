class Book:
    def __init__(self, author: str, title: str, book_id: int):
        self.author = author
        self.title = title
        self.book_id = book_id

    def __repr__(self):
        return f"Book(id={self.book_id}, author='{self.author}', title='{self.title}')"


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, book_id: int) -> bool:
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                return True
        return False

    def get_all_books(self):
        return self.books