isWorking = True
while(isWorking==True):
    a = int(input('Число I:'))
    x = input("Знак")
    b = int(input('Число II:'))
    if x == '-':
        print('Ответ:', a-b)
    elif x == '+':
        print('Ответ:', a+b)
    elif x == '/':
        print('Ответ:', a/b)
    elif x == '*':
        print('Ответ:', a*b)
    elif x == '%':
        print('Ответ:', a%b)
    elif x == '//':
        print('Ответ:', a//b)
    elif x == '**':
        print('Ответ:', a**b)
    else:
        print("'Неправильный знак.' \n 'Повторите еще раз.'")
