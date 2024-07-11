from abc import ABC, abstractmethod
from multipledispatch import dispatch

class Items(ABC):
    def __init__(self, title, author,price):  # I used the encapsulation by make the attributes protected and get & set functions
        self._title = title
        self._author = author
        self._price = price

    @abstractmethod  # I used abstraction here
    def get_title(self):  # I used polymorphism by makeing function with the same name but with different implementation
        pass
    @abstractmethod
    def get_author(self):
        pass
    @abstractmethod
    def get_price(self):
        pass
    @dispatch(str, str, float)   #I used the overloading here
    def set_all(self, title=None, author=None, price=None):
        pass
    @dispatch(str)
    def set_title(self, title):
        pass
    @dispatch(str)
    def set_author(self, author):
        pass
    @dispatch(float)
    def set_price(self, price):
        pass
    @abstractmethod
    def display(self):
        pass

class Book(Items):  # I used the inhertance here
    def __init__(self, title, author, price, isbn, genre,number_of_pages,inventory):  # I used the encapsulation by make the attributes private and get & set functions
        super().__init__(title, author, price)  # I inherit the attributes from the parent class
        self.__isbn = isbn
        self.__genre = genre
        self.__number_of_pages = number_of_pages
        inventory.add_item(self)

    def display(self):
        print(f"Title of book: {self.get_title()}")
        print(f"Author of book: {self.get_author()}")
        print(f"Price of book: {self.get_price()}")
        print(f"ISBN of book: {self.get_isbn()}")
        print(f"Genre of book: {self.get_genre()}")
        print(f"Number of Pages of book: {self.get_number_of_pages()}\n")

    def get_title(self):
        return self._title
    def get_author(self):
        return self._author
    def get_price(self):
        return self._price
    def get_isbn(self):
        return self.__isbn
    def get_genre(self):
        return self.__genre
    def get_number_of_pages(self):
        return self.__number_of_pages

    def set_all(self, title=None, author=None, price=None, isbn=None, genre=None, number_of_pages=None):
        if title != None:
            self._title = title
        if author != None:
            self._author = author
        if price != None:
            self._price = price
        if isbn != None:
            self.__isbn = isbn
        if genre != None:
            self.__genre = genre
        if number_of_pages != None:
            self.__number_of_pages = number_of_pages

    def set_title(self, title):
        self._title = title
    def set_author(self, author):
        self._author = author
    def set_price(self, price):
        self._price = price
    def set_isbn(self, isbn):
        self.__isbn = isbn
    def set_genre(self, genre):
        self.__genre = genre
    def set_number_of_pages(self, number_of_pages):
        self.__number_of_pages = number_of_pages

class Magazine(Items):  # I used the inhertance here
    def __init__(self, title, author, price, issue_number, publication_date,editor,inventory):  # I used the encapsulation by make the attributes private and get & set functions
        super().__init__(title, author, price)  # I inherit the attributes from the parent class
        self.__issue_number = issue_number
        self.__publication_date = publication_date
        self.__editor = editor
        inventory.add_item(self)

    def display(self):
        print(f"Title of magazine: {self.get_title()}")
        print(f"Author of magazine: {self.get_author()}")
        print(f"Price of magazine: {self.get_price()}")
        print(f"Issue number of magazine: {self.get_issue_number()}")
        print(f"Publication date of magazine: {self.get_publication_date()}")
        print(f"Editor of magazine: {self.get_editor()}\n")

    def get_title(self):
        return self._title
    def get_author(self):
        return self._author
    def get_price(self):
        return self._price
    def get_issue_number(self):
        return self.__issue_number
    def get_publication_date(self):
        return self.__publication_date
    def get_editor(self):
        return self.__editor

    def set_all(self, title=None, author=None, price=None, issue_number=None, publication_date=None, editor=None):
        if title != None:
            self._title = title
        if author != None:
            self._author = author
        if price != None:
            self._price = price
        if issue_number != None:
            self.__issue_number = issue_number
        if publication_date != None:
            self.__publication_date = publication_date
        if editor != None:
            self.__editor = editor

    def set_title(self, title):
        self._title = title
    def set_author(self, author):
        self._author = author
    def set_price(self, price):
        self._price = price
    def set_issue_number(self, issue_number):
        self.__issue_number = issue_number
    def set_publication_date(self, publication_date):
        self.__publication_date = publication_date
    def set_editor(self, editor):
        self.__editor = editor

class DVD(Items):  # I used the inhertance here
    def __init__(self, title, author, price, director, duration,genre,inventory):  # I used the encapsulation by make the attributes private and get & set functions
        super().__init__(title, author, price)  # I inherit the attributes from the parent class
        self.__director = director
        self.__duration = duration
        self.__genre = genre
        inventory.add_item(self)

    def display(self):
        print(f"Title of DVD: {self.get_title()}")
        print(f"Author of DVD: {self.get_author()}")
        print(f"Price of DVD: {self.get_price()}")
        print(f"Director number of DVD: {self.get_director()}")
        print(f"Duration of DVD: {self.get_duration()}")
        print(f"Genre of DVD: {self.get_genre()}\n")

    def get_title(self):
        return self._title
    def get_author(self):
        return self._author
    def get_price(self):
        return self._price
    def get_director(self):
        return self.__director
    def get_duration(self):
        return self.__duration
    def get_genre(self):
        return self.__genre

    def set_all(self, title=None, author=None, price=None, director=None, duration=None, genre=None):
        if title != None:
            self._title = title
        if author != None:
            self._author = author
        if price != None:
            self._price = price
        if director != None:
            self.__director = director
        if duration != None:
            self.__duration = duration
        if genre != None:
            self.__genre = genre

    def set_title(self, title):
        self._title = title
    def set_author(self, author):
        self._author = author
    def set_price(self, price):
        self._price = price
    def set_director(self, director):
        self.__director = director
    def set_duration(self, duration):
        self.__duration = duration
    def set_genre(self, genre):
        self.__genre = genre

class Inventory:
    def __init__(self):
        self.items=[]
        self.books=[]
        self.magazines=[]
        self.dvds=[]

    @dispatch(Book)
    def add_item(self,item):
            self.items.append(item)
            self.books.append(item)
        
    @dispatch(Magazine)
    def add_item(self,item):
        self.items.append(item)
        self.magazines.append(item)

    @dispatch(DVD)
    def add_item(self,item):
        self.items.append(item)
        self.dvds.append(item)

    def is_available(self,item):
        flag=False
        index=None
        for i in self.items:
            if i.get_title().lower() == item.get_title.lower():
                flag=True
                index=i
                break
        return (flag,index)

    def search_by_title(self, title):
        found_items = []
        for item in self.items:
            if item.get_title().lower() == title.lower():
                found_items.append(item)
        print(f"Search for Title = {title}:")
        print(len(found_items),"is found:\n")
        for item in found_items:
            item.display()
            print("")

    def search_by_author(self, author):
        found_items = []
        for item in self.items:
            if item.get_author().lower() == author.lower():
                found_items.append(item)
        print(f"Search for Author = {author}:")
        print(len(found_items), "is found:\n")
        for item in found_items:
            item.display()
            print("")

    def search_by_genre_for_books(self, genre):
        found_items = []
        for item in self.books:
            if item.get_genre().lower() == genre.lower():
                found_items.append(item)
        print(f"Search for Genre of Books = {genre}:")
        print(len(found_items), "is found:\n")
        for item in found_items:
            item.display()
            print("")

    def search_by_genre_for_dvds(self, genre):
        found_items = []
        for item in self.dvds:
            if item.get_genre().lower() == genre.lower():
                found_items.append(item)
        print(f"Search for Genre of DVDs = {genre}:")
        print(len(found_items), "is found:\n")
        for item in found_items:
            item.display()
            print("")

    def display_items(self):
        print("Inventory of items contain: (",end="")
        for i in range(len(self.items)):
            item =self.items[i]
            if i==len(self.items)-1:
                print(item.get_title(), end="")
            else:
                print(item.get_title(),",", end="")
        print(")\n")

    def display_books(self):
        print("Inventory of books contain: (",end="")
        for i in range(len(self.books)):
            item =self.books[i]
            if i==len(self.books)-1:
                print(item.get_title(), end="")
            else:
                print(item.get_title(),",", end="")
        print(")\n")
    
    def display_magazines(self):
        print("Inventory of magazines contain: (",end="")
        for i in range(len(self.magazines)):
            item =self.magazines[i]
            if i==len(self.magazines)-1:
                print(item.get_title(), end="")
            else:
                print(item.get_title(),",", end="")
        print(")\n")

    def display_dvds(self):
        print("Inventory of dvds contain: (",end="")
        for i in range(len(self.dvds)):
            item =self.dvds[i]
            if i==len(self.dvds)-1:
                print(item.get_title(), end="")
            else:
                print(item.get_title(),",", end="")
        print(")\n")


class Order:
    def __init__(self,items,quantities,sale):
        self.items=items
        self.quantities=quantities
        self.sale=sale

    def total_price(self):
        total=0
        total_after_sales=0
        for i in range(len(self.items)):
            item = self.items[i]
            quantity = self.quantities[i]
            total += item.get_price() * quantity
            total_after_sales=total - total*(self.sale.sale/100)
        print(f"Total Price= {total}")
        print(f"Sale {self.sale.sale}%")
        print(f"Total Price after sale= {total_after_sales}\n")

class Customer:
    def __init__(self,name):
        self.name=name
        self.orders=[]

    def place_order(self,order):
        self.orders.append(order)

    def count_orders(self):
        return len(self.orders)

    def details(self):
        print("The Name: ", self.name)
        print("The No. of orders: ", self.count_orders(),"\n")

class Sale:
    def __init__(self,sale=0):
        self.sale=sale

try:
    inventory=Inventory()
    sale=Sale(10)
    book1 = Book("Book 1", "Author1", 20, "ISBN1", "Genre1", "No.of.pages1",inventory)
    book2 = Book("Book 2", "Author1", 15, "ISBN2", "Genre2", "No.of.pages2",inventory)
    book1.set_number_of_pages(300)
    magazine1 = Magazine("Magazine 1", "Author2", 20,"Issue number1","publication date1","Editor1",inventory)
    magazine1.set_publication_date("1/1/2024")
    dvd1 = DVD("DVD 1", "Author3", 60, "Director1", "Duration1", "Genre1",inventory)
    dvd1.set_duration("2.5 Hours")
except TypeError:
    print("The type of the value is not correct")
except RuntimeError:
    print("Run time error is detected")
except ValueError:
    print("please input a proper value")

dvd1.display()
inventory.search_by_title("Book 1")
inventory.search_by_author("Author2")
inventory.search_by_genre_for_books("Genre1")
inventory.search_by_genre_for_dvds("Genre1")
inventory.display_items()
inventory.display_books()
order1=Order([book1,magazine1,dvd1],[1,1,1],sale)
order1.total_price()
customer1=Customer("Yassin")
customer1.place_order(order1)
customer1.details()
