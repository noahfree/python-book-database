# name: Noah Free
# date: 4/28/2021
#       For this project, I created a book "database" that allows the user to store information about books' info. There
#       are three different primary operations which are creating books, querying the created books, and updating books. When
#       books are created, the user is prompted to input a title, author, number of pages, current page, genre, and rating.
#       When querying the books, the user can search by title, author, genre, or rating. If there are any results from the search,
#       they are printed and the main menu is shown below. Finally, to update a book you search by title, and then you are asked
#       to input the information for the book, updating what you like.
#
#       Please note that I created some sample books so that there are already books present for you to query and update. Additionally,
#       in order for books to be saved the program has to be closed properly.

# Imports the math module
import math
# Imports the Book.py module to use class 'Book'
import Book
# Imports the pickle module to serialize objects
import pickle

# function main() contains a loop that calls the base functions until the user chooses to exit the program
def main(database):
    print("\n\tWelcome to the Book Database\n")
    while(True):
        select = mainMenu()
        if select == 1:
            book = createBook(database)
            if book != None: database.append(book)
        elif select == 2:
            searchDatabase(database)
        elif select == 3:
            updateBook(database)
        else:
            break
    print("\n\tThank you for using the Book Database!\n\t")
    return database

# function mainMenu() presents the main menu and returns the input, error checking
def mainMenu():
    toggle = 0
    while (toggle != '1' and toggle != '2' and toggle != '3' and toggle != '4'):
        print("\n\tMain Menu\n\t  1) Add a book to the database\n\t  2) Query the database\n\t  3) Update the database\n\t  4) Exit database")
        toggle = input("\tWhat would you like to do? Input 1, 2, 3 or 4.\n\t")
    return int(toggle)

# function createBook() creates a Book object based on what the user inputs
def createBook(database):
    newBook = Book.Book()
    temp = input("\n\tEnter the book's name:\n\t")
    toggle = False
    query = None
    for book in database:
        if book.get_title() == temp:
            toggle = True
            query = book
            break
    if toggle:
        print("\n\tBook found in database:")
        createOutput(book)
        prompt = input("\tWould you like to continue with the input? (y/n)\n\t")
        if prompt != 'y' and prompt != 'Y' and prompt != 'yes' and prompt != 'Yes':
            return None
    newBook.set_title(temp)
    temp = input("\n\tEnter the book's author:\n\t")
    newBook.set_author(temp)
    while (True):
        try:
            temp = int(input("\n\tEnter the book's page count:\n\t"))
            break
        except Error:
            continue
    newBook.set_total(temp)
    temp = input("\n\tEnter the page you are currently on: (0 if not started)\n\t")
    try:
        temp = int(temp)
        if temp < 0 or temp > newBook.get_total():
            newBook.set_current(0)
        else:
            newBook.set_current(temp)
    except Error:
        newBook.set_current(0)
    temp = input("\n\tEnter the book's genre:\n\t")
    newBook.set_genre(temp)
    temp = input("\n\tRate the book from 1 to 10: (0 to set later)\n\t")
    try:
        temp = float(temp)
        if (temp >= 1 and temp <= 10):
            newBook.set_rating(temp)
        else:
            newBook.set_rating(0)
    except Error:
        newBook.set_rating(0)
    createOutput(0, newBook)
    query = input("\n\tSave book? Enter yes or no.\n\t")
    while query != "Yes" and query != "yes" and query != "No" and query != "no":
        query = input("\n\tSave book? Enter yes or no.\n\t")
    if query == "Yes" or query == "yes":
        print("\n\tBook saved!")
        return newBook
    else: return None

# function searchDatabase() asks the user to choose how to query the database
def searchDatabase(database):
    toggle = 0
    while (toggle != '1' and toggle != '2' and toggle != '3' and toggle != '4' and toggle != '5') and toggle != '6':
        print("\n\tDatabase Search\n\t  1) Title\n\t  2) Author\n\t  3) Genre\n\t  4) Rating\n\t  5) Show All Books\n\t  6) Exit Search")
        toggle = input("\tHow would you like to search the database?\n\t")
    if toggle == '1':
        titleSearch(database)
    elif toggle == '2':
        authorSearch(database)
    elif toggle == '3':
        genreSearch(database)
    elif toggle == '4':
        ratingSearch(database)
    elif toggle == '5':
        print("\n\n\t" + str(len(database)) + " Result(s):")
        for index, book in enumerate(database):
            createOutput(index + 1, book)

# function titleSearch() searches the database by title
def titleSearch(database):
    title = input("\n\tEnter a book title to search for:\n\t")
    books = list()
    for index, book in enumerate(database):
        if title in book.get_title():
            books.append(index)
    if len(books) == 0:
        print("\n\tNo search results.")
        return None
    print("\n\n\t" + str(len(books)) + " Result(s):")
    for index, value in enumerate(books):
        createOutput(index + 1, database[value])

# function authorSearch() searches the database by author
def authorSearch(database):
    author = input("\n\tEnter an author to search for:\n\t")
    books = list()
    for index, book in enumerate(database):
        if author in book.get_author():
            books.append(index)
    if len(books) == 0:
        print("\n\tNo search results.")
        return None
    print("\n\n\t" + str(len(books)) + " Result(s):")
    for index, value in enumerate(books):
        createOutput(index + 1, database[value])

# function genreSearch() searches the database by genre
def genreSearch(database):
    genre = input("\n\tEnter a genre to search for:\n\t")
    books = list()
    for index, book in enumerate(database):
        if book.get_genre() == genre:
            books.append(index)
    if len(books) == 0:
        print("\n\tNo search results.")
        return None
    print("\n\n\t" + str(len(books)) + " Result(s):")
    for index, value in enumerate(books):
        createOutput(index + 1, database[value])

# function ratingSearch() searches the database by a rating range
def ratingSearch(database):
    print("\n\tEnter a range to search for.")
    floor = input("\t  lower limit: (enter a value 1-9.9)\n\t  ")
    while True:
        try:
            if float(floor) < 1 or float(floor) >= 10:
                floor = input("\t  lower limit: (enter a value 1-9.9)\n\t  ")
            else: break
        except Error:
            floor = input("\t  lower limit: (enter a value 1-9.9)\n\t  ")
    ceiling = input("\t  upper limit (enter a value: 1.1-10)\n\t  ")
    while True:
        try:
            if float(ceiling) <= 1 or float(ceiling) > 10:
                ceiling = input("\t  upper limit: (enter a value 1.1-10)\n\t  ")
            else: break
        except Error:
            ceiling = input("\t  upper limit: (enter a value 1.1-10)\n\t  ")
    books = list()
    for index, book in enumerate(database):
        if book.get_rating() == "None":
            continue
        elif float(book.get_rating()) >= float(floor) and float(book.get_rating()) <= float(ceiling):
            books.append(index)
    if len(books) == 0:
        print("\n\tNo search results.")
        return None
    print("\n\n\t" + str(len(books)) + " Result(s):")
    for index, value in enumerate(books):
        createOutput(index + 1, database[value])

# function updateBook() updates based on the user's inputs
def updateBook(database):
    while True:
        bookNum = -1
        title = input('\n\tEnter the title of the book to update: (input "back" to exit)\n\t')
        if title == "back" or title == "Back": break
        for index, book in enumerate(database):
            if title in book.get_title():
                bookNum = index
                break
        if bookNum != -1:
            createOutput(0, database[bookNum])
            toggle = input("\n\tUpdate this book? (y/n)\n\t")
            if toggle == 'y' or toggle == 'Y':
                database[bookNum] = createBook(list())
                return
        else:
            print("\n\tNo books found.")

# function createOutput() is the function used to output a book's information
def createOutput(num, book):
    if num == 0:
        print("\n\t" + book.get_title() + ", by " + book.get_author())
        print("\t   GENRE: " + str(book.get_genre()))
        print("\t   LENGTH: " + str(book.get_total()) + " pages")
        print("\t   PROGRESS: " + str(book.get_progress()))
        print("\t   RATING: " + str(book.get_rating()))
    else:
        print("\n\t" + str(num) + ")  " + book.get_title() + ", by " + book.get_author())
        print("\t     GENRE: " + str(book.get_genre()))
        print("\t     LENGTH: " + str(book.get_total()) + " pages")
        print("\t     PROGRESS: " + str(book.get_progress()))
        print("\t     RATING: " + str(book.get_rating()))


# below is where the object serialization is done, & where main() is called
try:
    with open('books.dat', 'rb') as books:
        try:
            bookList = pickle.load(books)
            books.close()
        except EOFError:
            bookList = list()
except FileNotFoundError:
    bookList= list()
bookList = main(bookList)
with open('books.dat', 'wb') as books:
    pickle.dump(bookList, books)
    books.close()
