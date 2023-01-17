from datetime import date
while True:
    try:
        ano_atual = date.today().year
        ano_nascimento = int(input('Digite o ano de nascimento: '))
        if ano_nascimento <= 0:
            print('Digite um ano válido.')
            break
        
        idade = ano_atual - ano_nascimento

        if idade <= 9:
            print(f'Você tem {idade} anos e sua categoria é MIRIM.')
        elif  idade <= 14:
            print(f'Você tem {idade} anos e sua categoria é INFANTIL.')
        elif idade <= 19:
            print(f'Você tem {idade} anos e sua categoria é JÚNIOR.')
        elif idade <= 25:
            print(f'Você tem {idade} anos e sua categoria é SÊNIOR.')
        else:
            print(f'Você tem {idade} anos e sua categoria é MASTER.')
    except ValueError:
        print('Dígitos inválidos.')
