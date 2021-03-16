class publisher:
    def __init__(self):
        print("parent class")
class book(publisher):
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display(self):
         print("The title of the book is",self.title)
         print("The author of the book is ",self.author)
class pyton(book):
    def __init__(self,price,pages):
        self.price=price
        self.pages=pages
    def display(self):
        print("price of the book : ",self.price)
        print("Total pages of the book :",self.pages)
c=book("Learning python","khaled hussain")
c.display()
c=pyton(550,853)
c.display()
