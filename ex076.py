produtos = ('Coca cola', 12,
            'Guaraná Antártica', 10,
            'Fanta Uva', 10,
            'Fanta Laranja', 10,
            'Tobi', 6,
            'Kuat', 7,
            'Pepsi', 10,
            'Sprite', 10,
            'Guaravita', 2.5)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for item in range(0, len(produtos)):
    if item % 2 == 0:
        print(f'{produtos[item]:.<30}',end=' ')
    else:
        print(f'R${produtos[item]:>7.2f}')
print('-' * 40)