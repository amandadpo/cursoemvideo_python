
print('Calduladora')
print('#' * 30)
while True:
    num_1 = input('Digite o primeiro número: ')
    num_2 = input('Digite o segundo número: ')

    numeros_validos = None

    try:
        num_1 = float(num_1)
        num_2 = float(num_2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('Um ou ambos os números são inválidos.')
        continue

    operador = str(input('Digite o operador para ver a operação [+] [-] [*] [/]: '))

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 * num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif len(operador) > 1:
        print('Digite um operador válido!')
        continue
    else:
        print('Digite um operador válido!')
        continue

    sair = input('Quer sair? [s]im [n]ão: ').lower().startswith('s')
    if sair is True:
        break
print('Fim')
