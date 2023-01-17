while True:
    try:    
        preço_produto = float(input('Preço do produto: '))
        if preço_produto < 0:
            print('Digite o valor correto')
            break
        pagamento = int(input(' [1] Pagamento à vista \n [2] à vista no cartão \n [3] 2x no cartão \n [4] 3x ou mais no cartão \n Informe a condição de pagamento: '))
        if pagamento == 1:  
            preco_final = preço_produto - (preço_produto * 0.10)  
            print('O preço do produto é R$ {:.2f}. Você ganhou desconto de 10%! O valor final do produto é R$ {:.2f}'.format(preço_produto,preco_final))
        elif pagamento == 2:
            preco_final = preço_produto - (preço_produto * 0.05)
            print('O preço do produto é R$ {:.2f}. Você ganhou desconto de 5%! O valor final do produto é R$ {:.2f}'.format(preço_produto,preco_final))
        elif pagamento == 3:
            print('O preço do produto é R$ {:.2f}.'.format(preço_produto))
        elif pagamento == 4:
            parcelas = int(input('Quantas parcelas? '))
            valor_parcelamento = preço_produto/parcelas
            valor_parcelas = valor_parcelamento + (valor_parcelamento * 0.20)
            valor_final = valor_parcelas * parcelas
            print(f'O preço do produto é R$ {preço_produto:.2f}. Você terá 20% de juros. O valor final do produto é R$ {valor_final:.2f} que será pago em {parcelas} parcelas de R$ {valor_parcelas:.2f} por mês')
        else:
            print('Digite uma opção válida.')
    except ValueError:
        print('Dados inválidos.')