###Enumarate
string = 'O brasil e penta'
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])

lista2 = ['Luiz', 'Joao', 'Maria'
          ]

for indice, nome in enumerate(lista2):
    print(indice, nome)

n1, n2, n3 = lista2

print(n2)
