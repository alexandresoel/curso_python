"""



"""
#cpf = input('Digite seu cpf: ')
cpf = '05017573331'
cpf_completo = list(cpf)
soma_cpf = 0
cpf_temp = ''
for i, r in enumerate(range(10, 1, -1)):
    cpf_temp += cpf_completo[i]
    soma_cpf += int(cpf_completo[i]) * r

primeiro_digito = 11 - (soma_cpf % 11)
soma_cpf = 0
if primeiro_digito > 9:
    primeiro_digito = 0

cpf_temp += str(primeiro_digito)

for x, y in enumerate(range(11, 1, -1)):
    soma_cpf += int(cpf_temp[x]) * y

segundo_digito = 11 - (soma_cpf % 11)

if segundo_digito > 9:
    segundo_digito = 0

cpf_temp += str(segundo_digito)

if cpf == cpf_temp:
    print('Válido')
else:
    print('Inválido')
