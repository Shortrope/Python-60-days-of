class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return "{0} by {1} (Published: {2})".format(self.title, self.author, self.year)

