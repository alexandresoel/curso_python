horas = input('Digite as horas: ')

if horas.isnumeric():
    horas = int(horas)
    if horas > 23:
        print(f'{horas} não é uma hora válida')
    else:
        if 0 <= horas <= 11:
            print('Bom dia!')
        elif 12 <= horas <= 17:
            print('Boa tarde!')
        else:
            print('Boa noite!')
else:
    print(f'{horas} não é uma hora válida')
