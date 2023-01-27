cont = 0
from random import randint

print('=' * 25)
print('Vamos jogar PAR ou ÍMPAR?')
print('=' * 25)

while True:
    try:
        jogada = str(input('Você quer par [P] ou ímpar [I]: ')).strip().upper()[0]
        if jogada not in 'PI':
            print('Jogada inválida.')
            break
        jogador = int(input('Escolha o valor: '))
    except ValueError:
        print('Ops...Opção inválida.')
        print('=' * 25)
        break
    computador = randint(0,10)
    resultado = computador + jogador
    print(f'Computador: {computador}')
    print(f'Total: {resultado}')

    if resultado % 2 == 0 and jogada == 'P':
        print('Jogador GANHOU! Deu PAR.')
        cont += 1
        print('=' * 25) 
    
    elif resultado % 2 !=0 and jogada == 'I':
        print('Jogador GANHOU. Deu ÍMPAR.') 
        cont += 1
        print('=' * 25)

    else:
        print('Jogador PERDEU!')
        break
print(f'GAME OVER! Você venceu em {cont}x.')
    