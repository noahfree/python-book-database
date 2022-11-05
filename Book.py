# name: Noah Free
# date: 4/28/2021
# pawprint: nsfq94
# description: 'Book.py' defines class 'Book'

# class Book has a title, author, totalPages, currentPage, genre, and a rating, along with getter and setter functions
class Book:
    def __init__(self):
        self.__title = None
        self.__author = None
        self.__totalPages = None
        self.__currentPage = None
        self.__genre = None
        self.__rating = None
    # setter functions
    def set_title(self, title):
        self.__title = title
    def set_author(self, name):
        self.__author = name
    def set_total(self, total):
        self.__totalPages = total
    def set_current(self, current):
        self.__currentPage = current
    def set_genre(self, genre):
        self.__genre = genre
    def set_rating(self, rating):
        self.__rating = rating
    # getter functions    
    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def get_total(self):
        return self.__totalPages
    def get_current(self):
        return self.__currentPage
    def get_progress(self):
        if self.__totalPages != 0:
            return str("{:.1f}".format((self.__currentPage / self.__totalPages)*100)) + "%"
        return "100.0%"
    def get_genre(self):
        return self.__genre
    def get_rating(self):
        if self.__rating == 0: return "None"
        return self.__rating