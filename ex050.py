soma = 0
cont = 0
for c in range(1,7):
    numero = int(input(f'Digite o {c}º número: '))
    if numero % 2 == 0:
        soma += numero
        cont += 1
print('Você informou {} números pares. A soma entre os números pares é {}'.format(cont,soma))