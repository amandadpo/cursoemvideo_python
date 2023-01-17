try:
    num_1 = float(input('Primeiro número: '))
    num_2 = float(input('Segundo número: '))
    if num_1 > num_2:
        print(f'{num_1} é maior que {num_2}')
    elif num_2 > num_1:
        print(f'{num_2} é maior que {num_1}')
    else:
        print(f'{num_1} é igual a {num_2}')
except ValueError:
    print('Digite apenas números')