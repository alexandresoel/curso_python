"""
Operadores Relacionais
== igualdade
>= maior ou igual
>  maior que
<  menor que
<= menor ou igual
!= diferente
"""
nome = input("Qual o seu nome? ")
idade = int(input("Qual é a sua idade? "))
valor = float(input("Qual o valor do emprestimo? "))

# Limite para pegar emprestimo
idade_limite = 18

if (idade >= idade_limite):
    print(f'{nome} pode pegar o empréstimo.')
    print(f'Você pegou R$ {valor:.2f} e terá que pagar R${valor * 1.25}')
else:
    print(f'{nome} NÃO PODE PEGAR O EMPRESTIMO.')
