numeros = []
pares = []
impares = []
for c in range(1,8):
    numeros.append(int(input(f'{c}º número: ')))
    for n in numeros:
        if n % 2 == 0:
            pares.append(numeros[:])
            numeros.clear()
        else:
            impares.append(numeros[:])
            numeros.clear()
pares.sort()
impares.sort()         
print(f'Os números pares são: {pares}')
print(f'Os números ímpares são: {impares}')

#Solução 2

num = [[],[]]
valor = 0
for c in range(1,8):
    valor = int(input(f'{c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Pares: {num[0]}')
print(f'Ímpares: {num[1]}')
