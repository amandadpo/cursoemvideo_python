numeros = []
while True:
    num = int(input('Digite um número: '))
    
    if num in numeros:
        print('Número duplicado. Não vou adicionar.')
    else:
        numeros.append(num)
        print('Número adicionado com sucesso!')
        
    pergunta = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if pergunta == 'N':
        print('Encerrando...')
        break
    if pergunta not in 'SN':
        print('Digite uma opção válida.')
    
numeros.sort() 
print(f'Lista: {numeros}')