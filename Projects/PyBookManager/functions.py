def display_books(blist):
    for book in blist:
        print(book)

def add_book(book, blist):
    """
    Adds a book object to the list
    :param book: dict - title, author, year
    :param blist: list of book objects
    """
    blist.append(book)
    return blist

def search_books(term, blist):
    results = []
    for book in blist:
        if book.title.find(term) != -1 or book.author.find(term) != -1:
            results.append(book)
    for book in results:
        print(book)

def delete_book():
    print("Deleteing...")
