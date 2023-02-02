time = ('Palmeiras','Internacional','Fluminense',
        'Corinthians','Flamengo','Athletico-PR',
        'Atlético-MG','Fortaleza','São Paulo',
        'América-MG','Botafogo','Santos','Goiás',
        'Bragantino','Coritiba','Cuiabá','Ceará',
        'Atlético-GO','Avaí','Juventude')

print('-=' * 20)
print(f'Os 5 primeiros colocados foram: {time[0:5]}')
print('-=' * 20)
print(f'Os quatro ultimos colocados foram {time[-4:]}')
print('-=' * 20)
print(f'Os times em ordem alfabética {sorted(time)}')
print('-=' * 20)
print('O Flamengo está na {}ª posição'.format(time.index('Flamengo')+1))
print('-=' * 20)

