"""
Operadores Lógicos - Aula 4
and, or, not
in e not in
"""
a = 2
b = 2
c = 3

print(a == b and b < c )

# (verdadeiro e verdadeiro) = Verdadeiro - todas as comparações precisam ser verdadeiras

# Not - negação da proposição
a = ''
if not a:
    print('Por favor, preencha o valor de A.')

# in e not in

nome = 'Luiz Otavio'

if not 'u' in nome:
    print('Existe.')
else:
    print('Não existe')
