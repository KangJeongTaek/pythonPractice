import Method

while(True):
    inputNum = input('1. 도서 등록\n2. 도서 검색\n3. 도서 삭제\n4. 도서 확인\n5. 도서 구입 \n0.종료\n')
    if inputNum == '1':
        print('도서 등록 하겠습니다.')
        Method.registration()
    elif inputNum == '2':
        print('도서 검색하겠습니다.')
        Method.search()
    elif inputNum == '3':
        print('도서 삭제하겠습니다')
        Method.delete()
    elif inputNum == '4':
        print('도서 확인하겠습니다.')
        Method.confirmation()
    elif inputNum == '5':
        print('도서 구입하겠습니다.')
        Method.purChase()
    elif inputNum == '0':
        print('종료하겠습니다.')
        break
    else:
        print('잘못된 입력입니다.')
        




