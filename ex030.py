while True:
    try:
        numero = int(input('Digite um valor para ver se é par ou ímpar: '))
        resultado = numero % 2
        if resultado == 0:
            print(f'{numero} é par!')
        else:
            print(f'{numero} é ímpar!')
    except ValueError:
        print('Dígito inválido')