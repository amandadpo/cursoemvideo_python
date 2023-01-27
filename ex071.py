print('=' * 50)
print('{:^40}'.format('Banco Amandita'))
print('=' * 50)

valor = int(input('Qual valor a ser sacado? '))

if valor % 50 == 0:
    divisao = valor // 50
    print(f'{divisao} notas de 50')

elif valor % 20 == 0:
    divisao = valor // 20
    print(f'{divisao} notas de 20')

elif valor % 10 == 0:
    divisao = valor // 10
    print(f'{divisao} notas de 10')

elif valor % 1 == 0:
    divisao = valor // 1
    print(f'{divisao} notas de 1')

