with open ('text.txt',mode='r',encoding='utf-8') as f:

    print(f.readlines())
    print('')
    f.seek(0)
    print(f.read())
    