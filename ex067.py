
while True:
    try:
        n = int(input('Digite um número para ver a tabuada: '))
    except ValueError:
        print('Digite apenas números.')
        continue

    if n < 0:
        print('Fim do programa.')
        break

    for cont in range(0,11):
        print(f'{n} x {cont} = {n*cont}')
    
    print('-' * 40)