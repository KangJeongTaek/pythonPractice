import shutil
import os

allbook = './BookTxt/Allbook.txt'
paperbook = './BookTxt/Paperbook.txt'
ebook = './BookTxt/Ebook.txt'
alltemp = './BookTxt/tamp.txt'
paperbooktamp = './BookTxt/temp_pbook.txt'
ebooktamp = './BookTxt/tamp_ebook.txt'

def clean():
    try:
        os.remove(ebooktamp)
    except FileNotFoundError as e:
        pass
    try:
        os.remove(alltemp)
    except FileNotFoundError as e:
        pass
    try:
        os.remove(paperbooktamp)
    except FileNotFoundError as e:
        pass


def update_inventory(book_name,bookType,original_file,temp_file):
    with open(original_file,mode='r',encoding='utf-8') as f_original,open(temp_file,mode='w',encoding='utf-8') as f_temp:
        stockout = False
        for line in f_original.readlines():
            book_info = line.strip().split(',')
            if int(book_info[-1]) > 0:
                f_temp.write(line)
            else:
                stockout = True
        if stockout:
            print(f'{book_name}이(가) 품절됐습니다. {bookType} 재고에서 삭제합니다.')
    shutil.copy(temp_file,original_file)


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

    while True:
        stock = 0
        try:
            stock = int(input('재고를 입력하세요.'))
            if stock <= 0:
                print('1 이상의 숫자를 입력하세요.')
                continue
            break
        except ValueError:
            print('숫자를 입력하세요.')
    while(True):
        epCheck = input('1. 전자책 2. 종이책 : ')
        if epCheck == '1':
            device = input('호환 기기를 입력해주세요.')
            #Ebook 텍스트에 등록
            with open('./Booktxt/Ebook.txt',mode='a',encoding='utf-8') as f_ebook:
                f_ebook.write(f'{name},{author},{price},{publisher},{device},{stock}\n')

            #전체 책 목록에 등록
            sameBook = False
            # 같은 책 정보라면 재고만 증가
            with open(allbook,mode='r',encoding='utf-8') as f_ab, open(alltemp,mode='w',encoding='utf-8') as f_atemp:
                for line in f_ab.readlines():
                    book_info = line.strip().split(',')
                    if book_info[1] == name and book_info[2] == author and int(book_info[3]) == price and book_info[4] == publisher and book_info[5] == device:
                        book_info[-1] = str(stock + int(book_info[-1]))
                        sameBook = True
                        line = ','.join(book_info) +'\n'
                        f_atemp.write(line)

            if sameBook:
                shutil.copy(alltemp,allbook)
            elif not sameBook:
                with open('./BookTxt./Allbook.txt',mode='a',encoding='utf-8') as f_all:
                    f_all.write(f'Ebook,{name},{author},{price},{publisher},{device},{stock}\n')
            break
        elif epCheck == '2':
            while(True):
                try:
                    size = int(input('페이지를 입력해주세요 : '))
                    sameBook = False
                    #Paperbook 텍스트에 등록
                    # 같은 책 정보라면 재고만 증가
                    with open(paperbook,mode='r',encoding='utf-8') as f_pb, open(paperbooktamp,mode='w',encoding='utf-8') as f_ptemp:
                        for line in f_pb.readlines():
                            book_info = line.strip().split(',')
                            if book_info[0] == name and book_info[1] == author and int(book_info[2]) == price and book_info[3] == publisher and int(book_info[4]) == size:
                                book_info[-1] = str(stock + int(book_info[-1]))
                                sameBook = True
                                line = ','.join(book_info) +'\n'
                                f_ptemp.write(line)
                    if sameBook:
                            shutil.copy(paperbooktamp,paperbook)
                    elif not sameBook:
                            with open('./Booktxt/Paperbook.txt',mode='a',encoding='utf-8') as f_paper:
                                f_paper.write(f'{name},{author},{price},{publisher},{size},{stock}\n')
                    #전체 책 목록에 등록
                                
                    sameBook = False
                    with open(allbook,mode='r',encoding='utf-8') as f_ab, open(alltemp,mode='w',encoding='utf-8') as f_atemp:
                        for line in f_ab.readlines():
                            book_info = line.strip().split(',')
                            if book_info[1] == name and book_info[2] == author and int(book_info[3]) == price and book_info[4] == publisher and int(book_info[5]) == size:
                                book_info[-1] = str(stock + int(book_info[-1]))
                                sameBook = True
                                line = ','.join(book_info) +'\n'
                                f_atemp.write(line)

                    if sameBook:
                        shutil.copy(alltemp,allbook)
                    elif not sameBook:
                        with open('./BookTxt./Allbook.txt',mode='a',encoding='utf-8') as f_all:
                            f_all.write(f'Paperbook,{name},{author},{price},{publisher},{size},{stock}\n')
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
                print(f'재고 : {book_info[6]}')
                print('-' * 30)
                found = True
    if not found:
        print('찾으시는 책이 없습니다.')

def delete():
    deleteBookName = input('삭제하시려는 책의 이름을 적어주세요 : ')
    found = False # Allbook 에서 확인
    found2 = False # Ebook에서 확인
    found3 = False # Paperbook에서 확인
    temp_file = './Booktxt/temp.txt' #
    with open('./Booktxt/AllBook.txt',mode='r',encoding='utf-8') as f_all,open('./Booktxt/temp.txt',mode='w',encoding='utf-8') as f_temp,\
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
        shutil.move('./Booktxt/temp.txt','./Booktxt/AllBook.txt')
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
            print(f'재고 : {book_info[5]}')
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
            print(f'재고 : {book_info[5]}')
            print(f'-'*30)
    
def purchase():

    
    purchaseName = input('구매하실 책의 이름을 선택하세요: ')

    foundName = False
    execution = False
    with open(allbook,encoding='utf-8',mode = 'r') as f_all,open(alltemp,mode ='w',encoding='utf-8') as f_temp ,\
        open(paperbook,mode ='r',encoding = 'utf-8') as f_p, open(paperbooktamp,mode='w',encoding = 'utf-8')as f_ptamp,\
        open(ebook,mode='r',encoding='utf-8')as f_e,open(ebooktamp,mode='w',encoding='utf-8') as f_etamp:
        for lineA in f_all.readlines():
            book_infoA = lineA.strip().split(',')
            if book_infoA[1] == purchaseName:
                foundName = True
                try:
                    quantity = int(input('구매하실 수량을 입력하세요.'))
                    if quantity > int(book_infoA[6]):
                        print('재고가 부족합니다.')
                        break
                    elif quantity <= 0:
                        print('올바른 값을 입력해주세요.')
                        break
                    else:
                        execution = True

                        book_infoA[6] = str(int(book_infoA[6]) - quantity)
                        lineA = ','.join(book_infoA) + '\n'
                        f_temp.write(lineA)

                        f_p.seek(0)
                        for lineP in f_p.readlines():
                            book_infoP = lineP.strip().split(',')
                            if book_infoP[0] == purchaseName:
                                book_infoP[5] = str(int(book_infoP[5]) - quantity)
                                lineP = ','.join(book_infoP) + '\n'
                                f_ptamp.write(lineP)

                        f_e.seek(0)
                        for lineE in f_e.readlines():
                            book_infoE = lineE.strip().split(',')
                            if book_infoE[0] == purchaseName:
                                book_infoE[5] = str(int(book_infoE[5]) -quantity)
                                lineE = ','.join(book_infoE) +'\n'
                                f_etamp.write(lineE)



                except ValueError:
                    print('올바른 수량을 입력하세요.')
                    break


    if not foundName :
        print(f'{purchaseName}은 재고에 없는 책 제목입니다.')
    elif execution:
        shutil.copy(alltemp,allbook)
        shutil.copy(paperbooktamp,paperbook)
        shutil.copy(ebooktamp,ebook)
        print(f'{purchaseName}을(를) 구매했습니다.')
        update_inventory(purchaseName,'전체책',allbook,alltemp)
        update_inventory(purchaseName,'종이책',paperbook,paperbooktamp)
        update_inventory(purchaseName,'전자책',ebook,ebooktamp)
        
        