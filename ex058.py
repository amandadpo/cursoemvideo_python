from random import randint
from time import sleep
cont = 0

print('Vamos jogar! Tente advinhar o número que eu pensar!')
print("Computador pensando...")
sleep(1)
print('*' * 30)

computador = randint(0,10)
acertou = False

while not acertou:
 
    try:
        jogador = int(input('Digite um número de 0 a 10: '))
        cont += 1

        if jogador < 0 or jogador > 10:
            print('Digite somente números de 0 a 10')
            continue
            
        if jogador > computador:
            print('Menos... Tente de novo.')

        elif jogador < computador:
            print('Mais... Tente de novo.')


        elif jogador == computador:
            print('Parabéns! Você acertou!')
            print(f'Você pensou no nº {jogador} e eu também.')  
            print('Foram necessárias {} tentativas para acertar.'.format(cont))
            break

    except ValueError:
        print('Digite somente números.')
