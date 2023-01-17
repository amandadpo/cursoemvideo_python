from datetime import date
while True:
    try: 
        ano = int(input('Digite um ano para ver se é bissexto: '))
        bissexto = ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0

        if ano <= 0:
            print('Digite um ano válido')
        elif bissexto:
            print(f'{ano} é um ano bissexto!')
        else:
            print(f'{ano} não é um ano bissexto!')

    except ValueError:
        print('Digite apenas números.')