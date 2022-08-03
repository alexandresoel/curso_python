nome = input('Digite seu nome? ')

if nome.__len__() <= 4:
    print(f'{nome} seu nome é muito curto!')
elif 5 <= nome.__len__() <= 6:
    print(f'{nome} seu nome é normal!')
else:
    print(f'{nome} seu nome é muito grande')
