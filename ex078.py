valores = []
for c in range(0,5):
    valores.append(int(input(f'Digite o {c}º valor: ')))
print(f'Lista: {valores}')
print(f'O maior valor foi {max(valores)} na posição ', end='')
for i,v in enumerate(valores):
    if v == max(valores):
        print(i, end='')
print()
print(f'O menor valor foi {min(valores)} na posição ',end='')
for i,v in enumerate(valores):
    if v == min(valores):
        print(i, end='')


