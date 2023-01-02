frase = 'O Python é uma linguagem de programação'\
        'multiparadigma.'\
        'Python foi criado por Guido van Rossum.' .upper()

#print(frase.upper().count('PYTHON'))

i = 0
qtde_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ' '


while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtde_atual = frase.count(letra_atual)

    if qtde_apareceu_mais_vezes < qtde_atual:
        qtde_apareceu_mais_vezes = qtde_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print('A letra que apareceu mais vezes foi {}. Ela apareceu {}x'.format(letra_apareceu_mais_vezes,qtde_apareceu_mais_vezes))


