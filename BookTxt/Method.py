import Book
import shutil
ebooklist = []
paerperbooklist = []
def registration():
    print("-" * 30)
    name = input('도서 이름을 입력하세요 : ')
    author = input('저자 이름을 입력하세요 : ')
    while(True):
        try:
            price = int(input('가격을 입력하세요 : '))
            break
        except ValueError:
            print('숫자를 입력하세요.')
    publisher = input('출판사를 입력하세요 : ')
    while(True):
        epCheck = input('1. 전자책 2. 종이책 : ')
        if epCheck == '1': 
            device = input('호환 기기를 입력해주세요.')
            #Ebook 텍스트에 등록
            with open('./Booktxt/Ebook.txt',mode='a',encoding='utf-8') as f_ebook:
                f_ebook.write(f'{name},{author},{price},{publisher},{device}\n')
            #전체 책 목록에 등록
            with open('./BookTxt./Allbook.txt',mode='a',encoding='utf-8') as f_all:
                f_all.write(f'Ebook,{name},{author},{price},{publisher},{device}\n')
            break
        elif epCheck == '2':
            while(True):
                try:
                    size = int(input('페이지를 입력해주세요 : '))
                    #Paperbook 텍스트에 등록
                    with open('./Booktxt/Paperbook.txt',mode='a',encoding='utf-8') as f_paper:
                        f_paper.write(f'{name},{author},{price},{publisher},{size}\n')
                    #전체 책 목록에 등록
                    with open('./BookTxt./Allbook.txt',mode='a',encoding='utf-8') as f_all:
                        f_all.write(f'Paperbook,{name},{author},{price},{publisher},{size}\n')
                    break
                except ValueError:
                    print('숫자를 입력해주십시오')
            break
        else:
            print('1과 2중에 입력해주세요.')
    shutil.copy('./Booktxt/AllBook.txt','./Booktxt/AllBook_backup.txt')


def search():
    searchBookstr = input('찾으시려는 책의 이름이나 저자를 입력해주세요 : ')
    found = False
    with open('./Booktxt/AllBook.txt',mode='r',encoding='utf-8') as f_all:
        for item in f_all.readlines(): #한 줄을 요소로 가지는 리스트 생성
            book_info = item.strip().split(',') # 한 줄에서 \n을 삭제하고 ,을 기준으로 나눈 리스트를 생성
            if searchBookstr == book_info[1] or searchBookstr == book_info[2]: #1번 인덱스 = 책 이름, 2번 인덱스 = 저자 이름
                print(f'{"찾으시는 책의 정보":>13}')
                print('-' * 30)
                print(f'종류 : {book_info[0]}')
                print(f'도서명 : {book_info[1]}')
                print(f'저자명 : {book_info[2]}')
                print(f'가격 : {book_info[3]}')
                print(f'출판사 : {book_info[4]}')
                if book_info[0] == 'Ebook':
                    print(f'호환 기기: {book_info[5]}')
                elif book_info[0] == 'Paperbook':
                    print(f'페이지 수 : {book_info[5]}')
                print('-' * 30)
                found = True
    if not found:
        print('찾으시는 책이 없습니다.')  

def delete():
    deleteBookName = input('삭제하시려는 책의 이름을 적어주세요 : ')
    found = False
    found2 = False
    found3 = False
    temp_file = './Booktxt/temp.txt'
    with open('./Booktxt/AllBook.txt',mode='r',encoding='utf-8') as f_all,open(temp_file,mode='w',encoding='utf-8') as f_temp,\
    open('./Booktxt/Ebook.txt',mode='r',encoding='utf-8') as f_ebook, open('./Booktxt/temp_ebook.txt',mode='w',encoding='utf-8')as f_etemp,\
    open('./Booktxt/Paperbook.txt',mode='r',encoding='utf-8') as f_pbook, open('./Booktxt/temp_pbook.txt',mode='w',encoding='utf-8')as f_ptemp:
        for line in f_all.readlines():
            book_info = line.strip().split(',')
            if book_info[1] != deleteBookName:
                f_temp.write(line)
            else:
                found = True
        for line in f_ebook.readlines():
            book_info = line.strip().split(',')
            if book_info[0] != deleteBookName:
                f_etemp.write(line)
            else:
                found2 = True
        for line in f_pbook.readlines():
            book_info = line.strip().split(',')
            if book_info[0] != deleteBookName:
                f_ptemp.write(line)
            else: found3 = True
        
                
    if not found and not found2 and not found3:
        print(f'찾으시는 이름의 책이 없습니다.')
    else:
        shutil.copy('./Booktxt/AllBook.txt', './Booktxt/AllBook_backup.txt')
        shutil.move(temp_file,'./Booktxt/AllBook.txt')
        shutil.copy('./Booktxt/Ebook.txt','./Booktxt/Ebook_backup.txt')
        shutil.move('./Booktxt/temp_ebook.txt','./Booktxt/Ebook.txt')
        shutil.copy('./Booktxt/Paperbook.txt','./Booktxt/Paperbook_backup.txt')
        shutil.move('./Booktxt/temp_pbook.txt','./Booktxt/Paperbook.txt')
        print(f'{deleteBookName}을(를) 삭제했습니다.')

def confirmation():
    Ebook = './Booktxt/Ebook.txt'
    PaperBook = './Booktxt/Paperbook.txt'
    with open(Ebook,mode='r',encoding='utf-8') as f_ebook:
        print(f'{"전자책":>15}')
        print(f'-'*30)
        for line in f_ebook.readlines():
            book_info = line.strip().split(',')
            print(f'도서명 : {book_info[0]}')
            print(f'저자명 : {book_info[1]}')
            print(f'가격 : {book_info[2]}')
            print(f'출판사 : {book_info[3]}')
            print(f'호환기기 : {book_info[4]}')
            print(f'-'*30)
    with open(PaperBook,mode='r',encoding='utf-8') as f_pbook:
        print(f'{"종이책":>15}')
        print(f'-'*30)
        for line in f_pbook.readlines():
            book_info = line.strip().split(',')
            print(f'도서명 : {book_info[0]}')
            print(f'저자명 : {book_info[1]}')
            print(f'가격 : {book_info[2]}')
            print(f'출판사 : {book_info[3]}')
            print(f'페이지 수 : {book_info[4]}')
            print(f'-'*30)
    
def purChase():
    bookType = input('1. 전자책 | 2. 종이책')
    

            
        

            
            


    