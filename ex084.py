lista_temporaria = []
pessoas = []
pesado = leve = 0

while True:
    lista_temporaria.append(str(input('Nome: ')))
    lista_temporaria.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        pesado = leve = lista_temporaria[1]

    else:
        if lista_temporaria[1] > pesado:
            pesado = lista_temporaria[1]
        if lista_temporaria[1] < leve:
            leve = lista_temporaria[1]
    pessoas.append(lista_temporaria[:])
    lista_temporaria.clear()
     
    resposta = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break
    if resposta not in 'SN':
        print('Digite uma opção válida.')


print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O mais pesado tem {pesado} kg. Peso de: ')

for p in pessoas:
    if p[1] == pesado:
        print(f'[{p[0]}]', end=' ')
print(f'O mais leve pesa {leve} kg. Peso de: ')
print()

for p in pessoas:
    if p[1] == leve:
        print(f'[{p[0]}]')
print()




