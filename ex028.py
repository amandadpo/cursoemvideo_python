from random import randint
from time import sleep

print('Vamos jogar! Tente advinhar o número que eu pensar!')
print("Computador pensando...")
sleep(1)
print('*' * 30)

while True:
    try:
        computador = randint(0,5)
        jogador = int(input('Digite um número de 0 a 5: '))


        if jogador >= 0 and jogador <= 5:
            if computador == jogador:
                print('Parabéns! Você acertou!')
                print(f'Você digitou nº {jogador} e eu também.')
            else:
                print('Você errou!')
                print(f'Você digitou o nº {jogador} e eu pensei no nº {computador}')
        else:
            print('Digite somente números de 0 a 5')
    except ValueError:
        print('Dados inválidos')
