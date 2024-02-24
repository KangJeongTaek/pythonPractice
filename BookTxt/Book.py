class Book:

    __tax = 1.1
    def __init__(self,title,author,price,publisher):
        self.title = title
        self.author = author
        self.price = price
        self.publisher = publisher

    def getTitle(self):
        return self.title
    
    def getAuthor(self):
        return self.author
    
    def getPrice(self):
        return self.price
    
    def getPublisher(self):
        return self.publisher
    
    def getTax(self):
        return self.__tax
    
class Ebook(Book):

    def __init__(self,title,author,price,publisher,device):
        super().__init__(title,author,price,publisher)
        self.device = device

    def deviceInfo(self): return self.device

class PaperBook(Book):

    def __init__(self,title,author,price,publisher,size):
        super().__init__(title,author,price,publisher)
        self.size = size

    def sizeInfo(self):
        return self.size