cont = 0
soma = 0
numero = 0


numero = int(input('Digite um número positivo ou 999 para SAIR: '))

while numero != 999:
    soma += numero
    cont += 1 
    numero = int(input('Digite um número inteiro ou 999 para SAIR: '))

print('Foram exibidos {} números e a soma entre eles é {}'.format(cont,soma))

