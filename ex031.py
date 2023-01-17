while True:
    try:    
        viagem = float(input('Distância da viagem em Km: '))

        if viagem < 0:
            print('Digite apenas números positivos!')
        elif viagem <= 200:
            preco = viagem * 0.5
            print('O valor da sua viagem é R${:.2f}'.format(preco))
        else: 
            preco = viagem * 0.45
            print('O valor da sua viagem é R${:.2f}'.format(preco))
    except ValueError:
        print('Digite apenas números.')
