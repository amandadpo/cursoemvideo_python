soma = 0
lista = []
jogos = {}
lista_completa = []
while True:
    jogos.clear()
    lista.clear()
    
    jogos['Nome do jogador'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogos["Nome do jogador"]} jogou? '))

    if partidas > 0:
        for c in range(1,partidas+1):
            gol = int(input(f'Quantos gols na partida {c}: '))
            soma += gol
            lista.append(gol)
            jogos['Gols'] = lista[:]
            jogos['Total de gols'] = sum(lista)
           
    else:
        print(f'O jogador {jogos["Nome do jogador"]} ainda não teve nenhuma partida.')
    
    lista_completa.append(jogos.copy())
    
    while True:
        resposta = str(input('Quer continuar [S/N]: ')).upper().strip()
        if resposta in 'SN':
            break
        print('Digite apenas S ou N.')
    if resposta in 'N':
        break

print('-=' * 30)
print('Cód ', end='')
for i in jogos.keys():
    print(f'{i:<18} ',end='')
print()
print('-' * 60)
for k,v in enumerate(lista_completa):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<20}',end='')
    print()  
print('-' * 60) 
while True:
    busca = int(input('Mostrar dados de qual jogador ou 999 para sair? '))
    if busca == 999:
        break
    if busca > len(lista_completa):
        print(f'ERRO! Não existe jogador com o código {busca}!')
    else:
        print(f' -- Levantamento do jogador {lista_completa[busca]["Nome do jogador"]}:')
        for i,g in enumerate(lista_completa[busca]['Gols']):
            print(f'    => Na partida {i+1}, fez {g} gol(s).')
        print(f'    => Totalizando {jogos["Total de gols"]} gols.')

    print('-' * 60)        
print(' >> VOLTE SEMPRE <<')





    