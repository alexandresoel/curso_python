# Iniciar com letra, pode contrer números, separa _, letras minúsculas
nome = 'Luiz Otávio'
idade = 32
altura = 1.80
e_maior = idade > 18
peso = 80
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'de idade e seu IMC é:', imc)
print(f'{nome} tem {idade} anos de idade e seus IMC é: {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {}'.format(nome, idade, imc))
