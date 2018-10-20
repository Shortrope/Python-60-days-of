def display_books(blist):
    for book in blist:
        print(book)

def search_books():
    print("Searching...")

def add_book(book, blist):
    """
    Adds a book object to the list
    :param book: dict - title, author, year
    :param blist: list of book objects
    """
    blist.append(book)
    return blist

def delete_book():
    print("Deleteing...")