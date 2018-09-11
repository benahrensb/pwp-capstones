class User(object):
    def __init__(self, email, name):
        self.email = email
        self.name = name
        self.books = {}
    def __repr__(self):
        return "User: {name} Email: {email}Books read: {books}".format(name=self.name,email=self.email,books=len(self.books))
    def get_email(self):
        return self.email
    def change_email(self, alternate_email):
        alternate_email = self.email
        return "This user's emil has been changed to: {email}".format(email = alternate_email)
    def read_book(self, book, rating = None):
        self.books[book] = rating
    def get_average_rating(self):
        return sum([num for num in self.books.values() if num is not None]) / len(self.books)
    def __hash__(self):
        return hash((self.name, self.email))
    def __eq__(self, other_user):
        if self.name and self.email == other_user.name and other_user.email:
            return (self.name and self.email) and (other_user.name and other_user.email)
class Book(object):
    def __init__(self, isbn, title):
        self.isbn = isbn
        self.title = title
        self.ratings = []
    def __repr__(self):
        return "Title: {book}ISBN: {isbn}".format(book = self.title, isbn = self.isbn)
    def get_title(self):
        return self.title
    def get_isbn(self):
        return self.isbn
    def add_rating(self, rating):
        try:
            if 0 < rating <= 4:
                self.ratings.append(rating)
            else:
                return "Invalid Rating."
    def get_average_rating(self):
        return sum([rating for rating in self.ratings]) / len(self.ratings)
    def __hash__(self):
        return hash((self.title, self.isbn))
    def __eq__(self, other_book):
        if ( self.isbn and self.title) == (other_book.isbn and other_book.title):
            return (self.isbn and self.title) and (other_book.title and other_book.isbn)
class Fiction(Book):
    def __init__(self, title, author, isbn):
        self.author = author
    def __repr__(self):
        return """Title: {title}
                  Author: {author} 
                  ISBN: {isbn}""".format(title = self.title,author = self.author, isbn = self.isbn)
    def get_author(self):
        return self.author
class NonFiction(Book):
    def __init__(self, title, subject, level, isbn):
        self.subject = subject
        self.level = level
    def __repr__(self):
        return """Title: {title}
                  Level: {level} 
                  Subject: {subject} 
                  ISBN: {isbn}\n""".format(title = self.title, level = self.level, subject = self.subject, isbn = self.isbn)
    def get_subject(self):
        return self.subject
    def get_level(self):
        return self.level
class TomeRater(object):
    def __init__(self):
        self.books = {}
        self.users = {}
    def __repr__(self):
        return "Users: {users_count} Books: {books_count}"
               "Total amount of times the books have been read: {reading_times}"\.format(users_count=len(self.users),books_count=len(self.books),reading_times=self.get_all_users_read_count())
    @staticmethod
    def create_book(title, isbn):
        return Book(title, isbn)
    @staticmethod
    def create_novel(title, author, isbn):
        return Fiction(title, author, isbn)
    @staticmethod
    def create_non_fiction(title, subject, level, isbn):
        return NonFiction(title, subject, level, isbn)
    def add_user(self, name, email, books = None):
        if email not in self.users:
            self.users[email] = User(name, email)
            if books is not None:
                for book in books:
                    self.add_book_to_user(book, email)
        else:
            print("This user already exists.")
    def add_book_to_user(self, book, email, rating=None):
        user = self.users.get(email, "No user with email: {email}".format(email = email))
        if user:
            book.add_rating(rating)
            user.read_book(book, rating)
    def print_catalog(self):
        for word in self.books.keys():
            print(word)
    def print_users(self):
        for name in self.users.values():
            print(name)
    def get_all_users_read_count(self):
        return sum([user.get_book_read_count() for user in self.users.values()])

    def most_read_book(self):
        return max(self.books, key = self.books.get())
    def __eq__(self, other_tomerater):
        return self.users == other_tomerater.users and self.books == other_tomerater.books
    
"""Dear CodeAcademy,
This is possibly the hardest coding challenge I have ever had to do.
thank you so much for offering this course, and I can gladly say that I have learned a lot.
I understand that the course finishes in a few weeks, therefore I plan on further editing this
code so that it runs more smoothly. Once again thank you so much and I hope that it does work.
Please note that there is an indentation error which doesn't seem to go away, I have tried
copying the code between shells to see if it worked better, but no result. 
Kind regards,

Ben Ahrens"""
