import moeda

p = float(input('Digite o preço R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p,True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p,True)}')
print(f'Aumentando 10% de {moeda.moeda(p)} temos {moeda.aumentar(p,True)}')
print(f'Reduzindo 13% de {moeda.moeda(p)} temos {moeda.diminuir(p, True)}')
