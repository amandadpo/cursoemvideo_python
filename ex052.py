cont = 0

numero = int(input('Digite um número: '))
for c in range(1,numero +1):
    
    if numero % c == 0:
        print('\033[34m', end='')
        cont += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c),end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(numero, cont))
if cont == 2:
    print('E por isso ele é PRIMO.')
else:
    print('E por isso ele NÂO é PRIMO.')

