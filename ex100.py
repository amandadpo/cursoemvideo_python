from random import randint
numeros = []

def sorteia():
    for c in range(0,5):
        n = randint(1,100)
        numeros.append(n)
    print(numeros)

    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n  
    print(f'A soma entre todos os pares é {soma}.')

sorteia()

