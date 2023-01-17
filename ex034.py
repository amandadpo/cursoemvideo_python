while True:
    try:
        salario = float(input('Digite o salário R$ '))
        if salario < 0:
            print('Digite um salário válido!')
        elif salario > 1250:
            aumento = (salario * 0.10) + salario
            print('Devido ao reajuste de 10%, o salário de R$ {:.2f} passou a valer R$ {:.2f}'.format(salario,aumento))
        else:
            aumento = (salario * 0.15) + salario
            print('Devido ao reajuste de 15%, o salário de R$ {:.2f} passou a valer R$ {:.2f}'.format(salario,aumento))
    except ValueError:
        print('Dados inválidos!')