lanche = ('hamburguer','suco','pizza','pudim')
print(lanche)
print('-' * 50)
print(lanche[1])
print('-' * 50)
print(lanche[-2])
print('-' * 50)
print(lanche[1:3])
print('-' * 50)
print(lanche[:2])
print('-' * 50)
print(lanche[-2:])
print('-' * 50)
#tuplas são imutáveis
for comida in lanche:
    print(comida)

print('-' * 50)
print(len(lanche))
print('-' * 50)

for cont in range(0,len(lanche)):
    print(lanche[cont])
    print(f'Eu vou comer {lanche[cont]}')
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

print('-' * 50)
print(sorted(lanche))
print('-' * 50)

a = (1,5,8)
b = (5,7,3,2)
c = a + b
print(c)
print(len(c))
print(c.count(5))
print(c.index(5))
print(c.index(1))
