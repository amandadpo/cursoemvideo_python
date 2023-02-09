palavras = ('amor','alegria','paz','felicidade',
         'sinceridade','sucesso','aprendizado',
         'Deus','prosperidade','amizade','cooperar',
         'fé','colaboração')

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos as vogais: ', end='')
    for letra in palavra: 
        if letra in 'aáàâãeéêiíoóõuú':
            print(letra, end=' ')