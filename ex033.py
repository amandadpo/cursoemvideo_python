
try:
    while True:
        a = float(input(f'Digite o 1º valor: '))
        b = float(input(f'Digite o 2º valor: '))
        c = float(input(f'Digite o 3º valor: '))

        if a > b and a > c:
            print(f'O número {a} é o maior entre eles.')
        elif b > a and b > c:
            print(f'O número {b} é o maior entre eles.')
        else:
            print(f'O número {c} é o maior entre eles.')    
        
        if a < b and a < c:
            print(f'O número {a} é o menor entre eles.')
        elif b < a and b < c:
            print(f'O número {b} é o menor entre eles.')
        else:
            print(f'O número {c} é o menor entre eles.')  
except ValueError:
    print('Digite apenas números!')
