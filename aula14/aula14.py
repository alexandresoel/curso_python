num1 = input('digite um número: ')
num2 = input('digite um número: ')

if num1.isnumeric() and num2.isnumeric():
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
else:
    print('Favor digitar apenas números')
