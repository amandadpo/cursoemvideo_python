import os

palavra_secreta = 'perfume'
letras_corretas = ''
tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue

    if letra_digitada in palavra_secreta:
        letras_corretas += letra_digitada
    elif letra_digitada is not palavra_secreta:
        print(f'Você errou. Não tem {letra_digitada} na palavra secreta.')
  
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_corretas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(f'Palavra formada:{palavra_formada}')

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print(f'Você ganhou! A palavra secreta é {palavra_secreta}!')
        print(f'Você precisou de {tentativas} tentativas')
        letras_corretas = ''
        numero_tentativas = 0



