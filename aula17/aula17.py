"""
Split, join, Enumerate em python
* Split dividir uma string
* Join - Juntar uma lista
* Enumarate - Enumerar elementos da lista # iteraveis
função strip = apaga os espaços em branco do início e fim


"""
string = 'O Brasil é o pais do futebol, o Brasil é o penta'
lista_2 = string.split(',')
lista_1 = string.split(' ')
palavra = ''
contagem = 0
for valor in lista_1:
    qnt_vezes = lista_1.count(valor)

    if qnt_vezes > contagem:
        contagem = qnt_vezes
        palavra = valor

print(f'A palavra {palavra} é a maior e apareceu {contagem} vezes')
