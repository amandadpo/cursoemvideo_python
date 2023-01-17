frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
inverso = junto[::-1]
print('o inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print('É palíndromo!')
else:
    print('Não é palíndromo')