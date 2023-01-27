soma = cont = 0

while True:
    try:
        numeros = int(input('Digite um valor: '))
    except ValueError:
        print('Digite apenas números.')
        continue

    if numeros == 999:
        break

    soma += numeros
    cont += 1

print(f'Você digitou {cont} números e a soma deles é {soma}.')