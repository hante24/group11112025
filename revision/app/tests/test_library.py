from revision.app.library import Book, Library

class TestBook:
    def test_book_attributes(self):
        book = Book(author="George Orwell", title="1984", book_id=1)

        assert book.author == "George Orwell"
        assert book.title == "1984"
        assert book.book_id == 1


class TestLibrary:

    def setup_method(self):
        self.library = Library("Central Library")
        self.book1 = Book("Author A", "Title A", 1)
        self.book2 = Book("Author B", "Title B", 2)

    def test_add_book(self):
        self.library.add_book(self.book1)

        assert len(self.library.books) == 1
        assert self.library.books[0].book_id == 1

    def test_add_multiple_books(self):
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)

        assert len(self.library.books) == 2

    def test_remove_book_success(self):
        self.library.add_book(self.book1)

        result = self.library.remove_book(1)

        assert result is True
        assert len(self.library.books) == 0

    def test_remove_book_not_found(self):
        self.library.add_book(self.book1)

        result = self.library.remove_book(999)

        assert result is False
        assert len(self.library.books) == 1

    def test_get_all_books(self):
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)

        books = self.library.get_all_books()

        assert len(books) == 2
        assert books[0].title == "Title A"
        assert books[1].title == "Title B"

