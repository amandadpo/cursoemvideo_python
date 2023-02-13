lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    pergunta = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if pergunta in 'N':
        break
    if pergunta not in 'SN':
        print('Digite uma opção válida!')
print(f'Foram digitados {len(lista)} números na lista.')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente {lista}')
if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')