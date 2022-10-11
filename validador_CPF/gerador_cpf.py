from random import randint

numero = randint(100000000, 999999999)

cpf_novo = str(numero)  #elimina os dois ultimos digitos
reverso = 10  #contador reverso
total = 0

for index in range(19):
    if index > 8:  #primeiro indice vai de 0 a 9
        index -= 9  #são os 9 primeiros digitos do cpf
    total += int(cpf_novo[index]) * reverso

    reverso -= 1
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:
            d = 0
        total = 0
        cpf_novo += str(d)

print(cpf_novo)
