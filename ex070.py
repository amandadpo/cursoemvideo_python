soma = cont = c = menor = barato = 0

print('=' * 40)
print('LOJA AMANDITA')
print('=' * 40)

while True:
    produto = str(input('Produto: ')).strip()

    preco = float(input('Preço: '))
    soma += preco
    cont += 1

    if preco > 1000:
        c += 1 

    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto

    opcao = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar [S/N]: ')).strip().upper()
    if opcao == 'N':
        print('Finalizando...')
        print('=' * 40)
        break
    
print(f'Total: R$ {soma:.2f}')
print(f'{c} produtos custam mais de R$ 1.000')
print(f'{barato.capitalize()} é o produto mais barato, custando R$ {menor:.2f}')