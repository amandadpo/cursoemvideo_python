from random import randint
from time import sleep
lista = []
jogos = []
cont = 0
total_jogos = 1
print('-' * 34)
print('     JOGO DA MEGA SENA     ')
print('-' * 34)

quant_jogos = int(input('Quantos jogos você quer sortear? '))
print('-=' * 3,f' Sorteando {quant_jogos} jogos ','-=' * 3)
print()

while total_jogos <= quant_jogos:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total_jogos += 1
for c,j in enumerate(jogos):
    print(f' Jogo {c+1}:{j}')
    sleep(1)
    
print('-' * 34)
print('-='* 4, '< Boa sorte! >','-='*4)










