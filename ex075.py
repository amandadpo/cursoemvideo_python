conj = (int(input('1º Número: ')),
        int(input('2º Número: ')),
        int(input('3º Número: ')),
        int(input('4º Número: ')))

print(f'Você digitou os números {conj}')
print(f'O número 9 apareceu {conj.count(9)}x.')
if 3 in conj:
    print(f'O número 3 apareceu na {conj.index(3)+1}ª posição.')
else:
    print('O número 3 não foi digitado em nenhuma das posições.')

print('Números pares: ', end='')
for c in conj:
    if c % 2 == 0:
        print(f'{c}  ', end='')
  



