opcao = 0


num_1 = float(input('Primeiro número: '))
num_2 = float(input('Segundo número: '))


while opcao != 5:
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    try:
        opcao = int(input('Digite a opção desejada: '))
    except ValueError or NameError:
        print('Digite apenas números')
        continue

    if opcao == 1:
        soma = num_1 + num_2
        print(f'{num_1} + {num_2} = {soma}')
    elif opcao == 2:
        multiplica = num_1 * num_2
        print(f'{num_1} * {num_2} = {multiplica}')
    elif opcao == 3:
        if num_1 > num_2:
            print(f'{num_1} é maior que {num_2}')
        else:
            print(f'{num_2} é maior que {num_1}')
    elif opcao == 4:
        try:
            num_1 = float(input('Primeiro número: '))
            num_2 = float(input('Segundo número: '))
        except ValueError or NameError:
            print('Digite apenas números')
    elif opcao == 5:
        print('Saindo...')
    else:
        print('Opção inválida. Tente novamente.')
print('=' * 20)        
print('FIM')