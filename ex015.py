km_rodado = int(input('Informe a quilometragem: '))
dias_alugado = int(input('Informe a quantidade de dias alugado: '))
preco_pagar = (dias_alugado * 60) + (km_rodado * 0.15)
print('O total a pagar pelo aluguel é R$ {:.2f}'.format(preco_pagar))