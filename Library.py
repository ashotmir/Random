from dataclasses import dataclass


all_books = []
all_students = []


class Book_init:

    def __init__(self, title, authors, year, ISBN, genre, copy=1, rating=5):
        self.title = title
        self.authors = authors
        self.year = year
        self.ISBN = ISBN
        self.genre = genre
        self.copy = copy
        self.rating = rating
        self.busy_copy = 0
        self.ID = len(all_books)
        all_books.append(self)

    def __repr__(self) -> str:
        return f"Title-{self.title} -- Authors-{self.authors}"


class Book_copy(Book_init):

    def borrow_copy(self):
        if self.available_copy() != 0:
            self.busy_copy += 1
            return self.busy_copy
        else:
            raise "Do not available copy"

    def _update_copy(self, other):
        all_books[self.ID].copy += other
        self.copy += other

    def return_copy(self):
        self.busy_copy -= 1

    def _change_id(self):
        for i in range(self.ID, len(all_books)):
            all_books[i].ID = i


class Book(Book_copy):

    def available_copy(self):
        available = self.copy - self.busy_copy
        return available

    def change_rating(self, other):
        old = all_books[self.ID].rating
        new = round((old + other) / 2, 1)
        all_books[self.ID].rating = new

    def add_new_copy(self):
        self.book._update_copy(self.count)

    def remove_copy(self):
        self.book._update_copy(-abs(self.count))

    def remove_book(self):
        all_books.pop(self.ID)
        self._change_id()


class Student:
    def __init__(self, name, ID, email) -> None:
        self.name = name
        self.ID = ID
        self.email = email
        self.taken_limit = 5
        self.all_brrowing_books = []
        self.taken_book = 0
        all_students.append(self.ID)

    def __repr__(self) -> str:
        return f"Name-{self.name}, ID-{self.ID}"

    def borrow_book(self, other: Book):
        if type(other) is not Book:
            raise TypeError
        elif self.taken_limit == 0:
            raise "out of limit"
        else:
            other.borrow_copy()
            self.all_brrowing_books.append(other)
            self.taken_limit -= 1
            self.taken_book += 1

    def return_book(self, other: Book):
        if type(other) is not Book:
            raise TypeError
        else:
            other.return_copy()
            self.taken_limit += 1
            self.taken_book -= 1


@dataclass
class Library(Book,Student):

    def add_book(self, title, authors, year, ISBN, genre, copy=1, rating=5):
        Book(title, authors, year, ISBN, genre, copy, rating)

    def add_student(self,name, ID, email):
        Student(name, ID, email)

    def remove_student(self,other):
        """other have to been student ID"""
        try:
            all_students.remove(other)
        except:
            print("Student not found")


    def change_borrowing_limit(self):
        pass

    def see_all_book():
        print(all_books)

    def available_books(self):
        pass


    def search_book(self, title=None, authors=None, year=None, ISBN=None, genre=None):
        pass



book_1 = Book(title="Lover", authors="Adam Smith", year=1954,
              ISBN=14514, genre="Romantic", copy=5)

student_1 = Student(name="Ashot",ID= 145414,email='ash@aca.org')
