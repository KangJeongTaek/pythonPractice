import Book

booklist = []
def registration():
    print("-" * 20)
    name = input('도서 이름을 입력하세요 : ')
    author = input('저자 이름을 입력하세요 : ')
    price = input('가격을 입력하세요 : ')
    publisher = input('출판사를 입력하세요 : ')
    while(True):
        epCheck = input('1. 전자책 2. 종이책 : ')
        if epCheck == '1':
            device = input('호환 기기를 입력해주세요.')
            book = Book.Ebook(name,author,price,publisher,device)
            booklist.append(book)
            break
        elif epCheck == '2':
            size = input('사이즈를 입력해주세요 : ')
            book = Book.PaperBook(name,author,price,publisher,size)
            booklist.append(book)
            break
        else:
            print('1과 2중에 입력해주세요.')


def search():
    searchBookName = input('찾으시려는 책의 이름이나 저자를 입력해주세요 : ')
    found = False
    for i in booklist:
        if i.getTitle() ==searchBookName or i.getAuthor() == searchBookName:
            found = True
            print('책을 찾았습니다.')
            print('-'*10)
            if isinstance(i,Book.Ebook):
                print(f'도서명 : {i.getTitle()}\n저자명 : {i.getAuthor()}\n가격 : {i.getPrice()}\n출판사 : {i.getPublisher()}\n호환 기기 : {i.deviceInfo()}')
            elif isinstance(i,Book.PaperBook):
                print(f'도서명 : {i.getTitle()}\n저자명 : {i.getAuthor()}\n가격 : {i.getPrice()}\n출판사 : {i.getPublisher()}\n호환 기기 : {i.sizeInfo()}')
            print('-'*10)

    if not found:
        print('찾으시는 책이 없습니다.')  

def delete():
    deleteBookName = input('삭제하시려는 책의 이름을 적어주세요 : ')
    found = False
    for i in booklist:
        if deleteBookName == i.getTitle():
            found = True
            print('-'*10)
            if isinstance(i,Book.Ebook):
                print(f'도서명 : {i.getTitle()}\n저자명 : {i.getAuthor()}\n가격 : {i.getPrice()}\n출판사 : {i.getPublisher()}\n호환 기기 : {i.deviceInfo()}를 삭제합니다.')
            elif isinstance(i,Book.PaperBook):
                print(f'도서명 : {i.getTitle()}\n저자명 : {i.getAuthor()}\n가격 : {i.getPrice()}\n출판사 : {i.getPublisher()}\n호환 기기 : {i.sizeInfo()}를 삭제합니다.')
            print('-'*10)    
            booklist.remove(i)
            print()
            print(f'{deleteBookName}를 삭제했습니다.')
            break
    
    if not found:
        print(f'찾으시는 이름의 책이 없습니다.')
    
            
            


    