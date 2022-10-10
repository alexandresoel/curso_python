usuario = input('Digite o seu nome: ')
senha = input('Digite a sua senha: ')

usuario_bd = 'alexandre'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema')
else:
    print('Usuário ou senha inválidos.')
