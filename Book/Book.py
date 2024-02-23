class Book:

    __tax = 1.1
    def __init__(title,author,price,publisher):
        self.title = title
        self.author = author
        self.price = price
        self.publisher = publisher

    def getTitle():
        return self.title
    
    def getAuthor():
        return self.author
    
    def getPrice():
        return self.price
    
    def getPublisher():
        return self.publisher
    
    def getTax():
        return self.__tax
    