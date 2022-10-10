# coding=utf-8
### Enumerate - enumerar elementos de uma lista
lista = [
    ['Edu', 'Joao', 'Luiz'],
    ['Maria', 'Tereza', 'Clare'],
    ['Lord', 'Jorgi', 'Priscila'],
]

enumerada = list(enumerate(lista))
print(enumerada[0][1][0])
