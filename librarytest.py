class Book:
    def __init__(self,title,author,available=True):
        self.title=title
        self.author=author
        self.available=available

class Library:
    def __init__(self):
        self.books=[]

    def add_book(self,book):
        self.books.append(book)

    def search_by_title(self,title):
        search_title = lambda book: book.title.lower() == title.lower()
        return list(filter(search_title, self.books))
    
    def search_by_author(self,author):
        search_author = lambda book: book.author.lower()==author.lower()
        return list(filter(search_author,self.books))
    
    def update_availability(self,title,available):
        update_book = lambda book:setattr(book,"available",available) if book.title.lower()==title.lower() else None
        list(map(update_book,self.books))

#List a list of books
book1=Book("Real Book", "Professor RandomName",False)
book2=Book("The real Book","FirstName SurName",True)
book3=Book("101 Ways to Score Touchdowns","The NFL Experts",True)

#create Library
library=Library()

#adding books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

#search by title and then search by author

print("Books with the title 'Real Book': ")
for book in library.search_by_title("Real Book"):
    print(f" {book.title} by {book.author}")

print("Books with the author 'The NFL Experts': ")
for book in library.search_by_author("The NFL Experts"):
    print(f" {book.title} by {book.author}")

#update availability of books
library.update_availability("Real Book",True)

#check the update went through
print("\n Availability  of 'Real Book': ")
for book in library.search_by_title("Real Book"):
    print(f"{book.title} is {'available' if book.available else 'not available'}")

#update availability of books
library.update_availability("101 Ways to Score Touchdowns",False)

#check the update went through
print("\n Availability  of '101 Ways to Score Touchdowns': ")
for book in library.search_by_title("101 Ways to Score Touchdowns"):
    print(f"{book.title} is {'available' if book.available else 'not available'}")
