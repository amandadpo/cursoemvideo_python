soma = 0
lista = []
jogos = {}
jogos['Nome do jogador'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogos["Nome do jogador"]} jogou? '))

if partidas > 0:
    for c in range(1,partidas+1):
        gol = int(input(f'Quantos gols na partida {c}: '))
        soma += gol
        lista.append(gol)
        jogos['Gols'] = lista
        jogos['Total de gols'] = sum(lista)

    print('-=' * 30)
    print(jogos)

    print('-=' * 30)
    for k,v in jogos.items():
        print(f'{k} = {v}')

    print('-=' * 30)
    print(f'O(a) jogador(a) {jogos["Nome do jogador"]} jogou {partidas} partidas.')
    for i,c in enumerate(lista):
        print(f'    => Na partida {i+1}, fez {c} gol(s).')

    print(f'Foi um total de {jogos["Total de gols"]} gol(s).')
else:
    print(f'O jogador {jogos["Nome do jogador"]} ainda não teve nenhuma partida.')

