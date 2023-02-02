from random import randint

numeros = (randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100))
print(f'Lista gerada: {numeros}')
print(f'O maior valor da lista é {max(numeros)}.')
print(f'O menor valor da lista é {min(numeros)}.')