import os
#from functions import display_books, search_books, add_book, delete_book
from book import Book

"""
The Book Manager keeps a list of Book data
- Title
- Author
- Year
The list starts empty and You can do the following
- Add a Book
- Delete a Book
- Display the list of Books
- Search for a Book
"""

"""
Application:
Use a list to store the books
Class 'Book' to define a book
Create functions to 
- add
- delete
- display
- search
"""

books = []

def display_books():
    for book in books:
        print(book)

def add_book(book):
    """
    Adds a book object to the list
    :param book: dict - title, author, year
    """
    books.append(book)

def search_books(term):
    results = []
    for book in books:
        if book.title.find(term) != -1 or book.author.find(term) != -1:
            results.append(book)
    for book in results:
        print(book)

def delete_book(title):
    for book in books:
        if book.title.find(title) != -1:
            del books[books.index(book)]
            return
    print(f"{title} not found.")

add_book(Book("HTML and CSS", "Mario Kaack", 2008))
add_book(Book("CCNP Training", "David Huckaby", 2012))
add_book(Book("Learning SQL", "Joe Piscapo", 2014))

def display_menu():
    os.system('clear')
    print('\n')
    print("What would you like to do?")
    print("1) View list of books")
    print("2) Search for a book")
    print("3) Add a book")
    print("4) Delete a book")
    print("q) Quit")

# Application loop
display_menu()
while True:
    # Display menu of actions
    action = input("\n(?) : ")
    display_menu()

    if action == "1":
        print()
        display_books()
        print()
    elif action == "2":
        print()
        search_term = input("Search Term: ")
        print()
        search_books(search_term)
        print()
    elif action == "3":
        print()
        print('Add Book:')
        title = input("Book Title: ")
        author = input("Book Author: ")
        year = input("Book Year: ")
        book = Book(title, author, year)
        add_book(book)
    elif action == "4":
        print()
        print("Delete:")
        title = input("Title: ")
        delete_book(title)
    elif action == "q" or action == "Q":
        os.system('clear')
        break
    else:
        print("Invalid Choice!")
