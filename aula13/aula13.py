usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print('Você precisa digitar pelo menos 6 caracteres')
else:
    print('Você foi cadastrado no sistema.')

string1 = input('Digite alguma coisa: ')
string2 = input('Digite alguma coisa: ')

print(len(string1))
print(string2.__len__())
