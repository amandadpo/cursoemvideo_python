import re
import sys
#cpf_usuario = input('Digite o CPF: ')\     ou usar o código abaixo
#    .replace('.','')\
#   .replace('-','')\
#    .replace('','')

entrada = input('Digite o CPF: ')
cpf_usuario = re.sub(r'[^0-9]', '',entrada)

entrada_sequencial = entrada == entrada[0] * len(entrada)
if entrada_sequencial:
    print('Você enviou dados sequenciais')
    sys.exit()

nove_digitos = cpf_usuario[:9]
contador_regressivo_1 = 10
resultado_digito_1 = 0

for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11

digito_1 = digito_1 if digito_1 <= 9 else 0
#print(digito_1)

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <=9 else 0
#print(digito_2)

cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_usuario == cpf_gerado:
    print(f'{cpf_usuario} é válido')
else:
    print('CPF inválido')






