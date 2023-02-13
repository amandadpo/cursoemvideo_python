lista = []
pares = []
impares = []

while True:
    try:
        n = (int(input('Digite um valor: ')))
        lista.append(n)
    except ValueError:
        print('Opção inválida') 
    pergunta = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]

    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
        
    if pergunta in 'N':
        break
    if pergunta not in 'SN':
        print('Opção inválida')

print(f'Lista: {lista}')
print(f'Lista de pares: {pares}')
print(f'Lista de ímpares: {impares}')