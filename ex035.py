print('=' * 40)
print('Analisador de triângulos')
print('=' * 40)

while True:
    try:
        a = float(input('Digite o tamanho da primeira reta: '))
        b = float(input('Digite o tamanho da segunda reta: '))
        c = float(input('Digite o tamanho da terceira reta: '))

        if a < b + c  and b < a + c and c < b + a:
            print('Com estas retas é possível construir um triângulo!')

        else:
            print('Com estas retas NÂo é possível construir um triângulo.')

    except ValueError:
        print('Digite apenas números.')