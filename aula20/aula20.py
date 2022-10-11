"""
Operador Ternario
"""

logged_user = True

msg = 'Usuario logado.' if logged_user else 'Usuario precisa fazer login.'

print(msg)


nome = input('Digite seu nome: ')
print (nome or 'Você nao digitou nada')
