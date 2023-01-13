while True:    
    try:
        velocidade = int(input("Digite a velocidade do carro: "))

        if velocidade < 0:
            print('DIgite uma velocidade válida!')
        elif velocidade > 80:
            multa = (velocidade - 80) * 7
            print('Você foi multado!')
            print(f'O valor da sua multa foi de R$ {multa:.2f}')
        else:
            print('Velocidade dentro da permitida.')
    except ValueError:
        print("Dados inválidos")