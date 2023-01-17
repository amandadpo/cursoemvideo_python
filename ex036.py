try:
    casa = float(input('Digite o valor da casa R$ '))
    salario = float(input('Informe o salário R$ '))
    anos = int(input('Informe em quantos anos irá pagar: '))
    prestacao_mensal = casa / (anos * 12)

    if casa <= 0 or salario <= 0 or anos <= 0:
        print('Um ou mais dados informados não é/são válidos.')
        
    elif prestacao_mensal > (salario*0.30) + salario:
        print('Empréstimo NEGADO')
    else:
        print('Empréstimo CONCEDIDO')
        print(f'O valor da prestação será R$ {prestacao_mensal:.2f}')
except ValueError:
    print('Dígito inválido.')
except ZeroDivisionError:
    print('Você digitou 0 no campo de anos. Digite um número válido.')


