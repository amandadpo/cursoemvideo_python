from random import randint
from time import sleep
try:
    computador = randint(0,2)

    print('Vamos jogar JOKENPO!')
    print('''Escolha uma das opções
    [0] Pedra
    [1] Papel
    [2] Tesoura
    ''')
    jogador = int(input('Faça sua jogada: '))
    if jogador < 0 or jogador > 2:
        print('Digite uma opção válida.')
        
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!')
    sleep(1)
    if jogador == computador:
        print('EMPATE!')
    elif jogador == 0 and computador == 2:
        print(f'JOGADOR ganhou! Computador escolheu TESOURA e você escolheu PEDRA')
    elif jogador == 0 and computador == 1:
        print(f'Computador ganhou! Computador escolheu PAPEL e você escolheu PEDRA')
    elif jogador == 1 and computador == 0:
        print(f'JOGADOR ganhou! Computador escolheu PEDRA e você escolheu PAPEL')
    elif jogador == 1 and computador == 2:
        print(f'Computador ganhou! Computador escolheu TESOURA e você escolheu PAPEL')
    elif jogador == 2 and computador == 0:
        print(f'Computador ganhou! Computador escolheu PEDRA e você escolheu TESOURA')
    elif jogador == 2 and computador == 1:
        print(f'JOGADOR ganhou! Computador escolheu PAPEL e você escolheu TESOURA')
    
except:
    print('Digite uma opção válida.')
    
