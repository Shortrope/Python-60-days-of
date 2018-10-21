from functions import display_books, search_books, add_book, delete_book
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

add_book(Book("HTML and CSS", "Mario Kaack", 2008), books)
add_book(Book("CCNP Training", "David Huckaby", 2012), books)
add_book(Book("Learning SQL", "Joe Piscapo", 2014), books)

# Application loop
while True:
    # Display menu of actions
    print("What would you like to do?")
    print("1) View list of books")
    print("2) Search for a book")
    print("3) Add a book")
    print("4) Delete a book")
    print("q) Quit")

    action = input("\n(?) : ")

    if action == "1":
        print()
        display_books(books)
        print()
    elif action == "2":
        search_term = input("Search Term: ")
        print()
        search_books(search_term, books)
        print()
    elif action == "3":
        title = input("Book Title: ")
        author = input("Book Author: ")
        year = input("Book Year: ")
        book = Book(title, author, year)
        add_book(book, books)
    elif action == "4":
        delete_book()
    elif action == "q" or action == "Q":
        print("Quiting...")
        break
    else:
        print("Invalid Choice!")
