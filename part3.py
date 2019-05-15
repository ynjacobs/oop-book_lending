from datetime import datetime
import random


class Book:

    on_shelf = []
    on_loan = []
    overdue_books = []

    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.due_date = None

    def borrow(self):
        #  if it i1s `lent_out` to check if the book is already on loan,
        #  return False to indicate that the attempt to borrow the book failed. 
        # Otherwise, 
        #   use `current_due_date` to set the due_date of the book
        # and move it from the collection of available books to the collection of books on loan, then return True.
        if self.lent_out():
            return False
        else:
            self.due_date = self.current_due_date()
            Book.on_shelf.remove(self)
            Book.on_loan.append(self)
        return True

    def return_to_library(self):
        if self.lent_out() is False:
            return False
        else:
            Book.on_loan.remove(self) and Book.on_shelf.append(self)
            self.due_date = None
            return True
        
    def lent_out(self):
        return self in Book.on_loan

    @classmethod
    def create(cls, book_tile, author, ISBN):
        my_new_book = Book(book_tile, author, ISBN)
        cls.on_shelf.append(my_new_book)
        return my_new_book

    @classmethod
    def current_due_date(cls):
        now = datetime.now()
        two_weeks = 60 * 60 * 24 * 14  # two weeks expressed in seconds
        future_timestamp = now.timestamp() + two_weeks
        return datetime.fromtimestamp(future_timestamp)

    @classmethod
    def over_due_books(cls):
        for book in Book.on_loan:
            if Book.current_due_date() < datetime.now():
                Book.overdue_books.append(book)

    @classmethod
    def browse(cls):
        return random.choice(cls.on_shelf)


# b1 = Book.create("Cat in the Hat", "Dr. Seuss", "dfasdfasdfadsfadsf")
# b2 = Book.create("Red Fish Blue Fish", "Dr. Seuss", "dfasdfa452345234534sdfadsfadsf")
# b3 = Book.create("Grinch Who Stole Chistmas", "Dr. Seuss", "253452345")

sister_outsider = Book.create("Sister Outsider", "Audre Lorde", "9781515905431")
aint_i = Book.create("Ain't I a Woman?", "Bell Hooks", "9780896081307")
if_they_come = Book.create("If They Come in the Morning", "Angela Y. Davis", "0893880221")
print(Book.browse().title)  # "Sister Outsider" (this value may be different for you)
print(Book.browse().title)  # "Ain't I a Woman?" (this value may be different for you)
print(len(Book.on_shelf))  # 3
print(len(Book.on_loan))  # 0
print(sister_outsider.lent_out())  # False
print(sister_outsider.borrow())  # True
print(len(Book.on_shelf))  # 2
print(len(Book.on_loan))  # 1
print(sister_outsider.lent_out())  # True
print(sister_outsider.borrow())  # False
print(sister_outsider.due_date)  # 2017-02-25 20:52:20 -0500 (this value will be different for you)
print(len(Book.overdue_books))  # 0
print(sister_outsider.return_to_library())  # True
print(sister_outsider.lent_out())  # False
print(len(Book.on_shelf))  # 2
print(len(Book.on_loan))  # 0