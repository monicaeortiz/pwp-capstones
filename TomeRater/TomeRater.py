class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("This user's email has been changed to:",self.email)

    def __repr__(self):
        return("User {user}, email: {email}, books read: {num_books}".format(user=self.name, email=self.email, num_books=len(self.books)))

    def __eq__(self, other_user):
        return self.email == other_user.email and self.name == other_user.email

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        rating_sum = 0
        for value in self.books.values():
            if type(value) == int:
                rating_sum += value
        return rating_sum/len(self.books.keys())

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn
        print("This book's isbn has been changed to:",self.isbn)

    def add_rating(self, rating):
        if rating is None:
            return

        if rating >=0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn

    def __hash__(self):
        return hash((self.title, self.isbn))

    def get_average_rating(self):
        rating_sum=0
        for rating in self.ratings:
            if type(rating) == int:
                rating_sum += rating

        try:
            return rating_sum/len(self.ratings)
        except ZeroDivisionError:
            return 0

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super(Fiction, self).__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        self.format = "{title} by {author}".format(title=self.title, author=self.author)
        return self.format

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super(Non_Fiction, self).__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)

class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def __repr__ (self):
        return "There are {num_users} users and {num_books} in the catalog.".format(num_users=len(self.users.keys()), num_books=len(self.books.keys()))

    def __eq__(self, other_TomeRater):
        return sorted(list(self.users.keys())) == sorted(list(other_TomeRater.users.keys()))

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        try:
            current_user = self.users[email]
            current_user.read_book(book, rating)
            book.add_rating(rating)
            try:
                self.books[book] += 1
            except KeyError:
                self.books[book] = 1
                book_list = list(self.books.keys())
        except KeyError:
            print("No user with email {email}".format(email=email))

    def add_user(self, name, email, user_books=None):

        if "@" not in email or not (".com" in email or ".edu" in email or ".org" in email):
            print("Invalid email address.")
            return
        if email in self.users.keys():
            print("A user with this email already exists.")
            return
        else:
            self.users[email] = User(name, email)
            if user_books != None:
                for book in user_books:
                    self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        most_reads = 0
        best_book = None
        for book in self.books.keys():
            if self.books[book] > most_reads:
                most_reads = self.books[book]
                best_book = book
        return best_book

    def highest_rated_book(self):
        max_rating=0
        best_book = None
        for book in self.books.keys():
            if book.get_average_rating() > max_rating:
                max_rating = book.get_average_rating()
                best_book = book
        return best_book

    def most_positive_user(self):
        highest_ratings = 0
        highest_rater = None
        for user in self.users.values():
            if user.get_average_rating() > highest_ratings:
                highest_ratings = user.get_average_rating()
                highest_rater = user
        return highest_rater



