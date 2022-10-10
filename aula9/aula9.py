"""
Entrada de dados
"""
# o print retorna apenas string
nome = input("Qual o seu nome? ")
idade = input("Qual é a sua idade? ")

print (f'{nome} tem {idade} anos.')

ano_nascimento = 2022 - int(idade)
print(f'{nome} nasceu em {ano_nascimento}')
