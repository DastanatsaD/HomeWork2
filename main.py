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
    print("Повторите еще раз")