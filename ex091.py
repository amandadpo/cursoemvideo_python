from random import randint
from time import sleep
from operator import itemgetter
dado = {'Jogador1': randint(1,6),
        'Jogador2': randint(1,6),
        'Jogador3': randint(1,6),
        'Jogador4': randint(1,6)}
ranking = []
print('Valores sorteados:')
for k,v in dado.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
print('-='* 20)
print(' == Ranking dos jogadores == ')
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)
for i,v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)

