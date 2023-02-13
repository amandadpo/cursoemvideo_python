numeros = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > numeros[-1]:
        numeros.append(n)
        print('Adicionado ao final da lista')
    else:
        posicao = 0
        while posicao < len(numeros):
            if n <= numeros[posicao]:
                numeros.insert(posicao,n)
                print(f'Adicionado na posição {posicao} da lista')
                break
            posicao += 1 
print(f'Os valores digitados em ordem foram {numeros}')




