nome = 'Alexandre Trajano'
idade = 29
altura = 1.63
peso = 90.00
ano_atual = 2022
ano_nascimento = ano_atual - idade
imc = peso / (altura ** 2)

print(f'{nome} tem {altura} de altura e {peso} kg e seu imc é de: {imc:.2f} e ele nasceu em {ano_nascimento}')
