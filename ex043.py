while True:
    try:
        peso = float(input('Digite seu peso: '))
        altura = float(input('Digite sua altura: '))
        if peso or altura <= 0:
            print('Peso e/ou altura inválidos.')
            continue
        
        imc = peso / (altura ** 2)

        if imc < 18.5:
            print(f'Seu IMC é {imc:.2f} e Você está ABAIXO DO PESO.')
        elif imc < 25:
            print(f'Seu IMC é {imc:.2f} e Você está NO PESO IDEAL.')
        elif imc < 30:
            print(f'Seu IMC é {imc:.2f} e Você está em SOBREPESO.')  
        elif imc < 40:
            print(f'Seu IMC é {imc:.2f} e Você está em OBESIDADE.') 
        elif imc > 40:
            print(f'Seu IMC é {imc:.2f} e Você está em OBESIDADE MÓRBIDA.')
    except ValueError:
        print('Dados inválidos.')
