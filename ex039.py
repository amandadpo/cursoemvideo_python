from datetime import date
try:
    ano_atual = date.today().year
    ano_nascimento = int(input('Digite seu ano de nascimento: ')) # resolver caso o usuário digite um ano invalido
    anos = ano_atual - ano_nascimento
    if anos > 18:
        alistamento = anos - 18
        print('Você tem/terá {} anos neste ano. Seu tempo de alistamento já passou há {} anos.'.format(anos,alistamento))
        print('Seu ano de alistamento foi em {}.'.format(ano_atual - alistamento))
    elif anos < 18:
        alistamento = 18 - anos
        print('Você tem/terá {} anos neste ano e deverá se alistar daqui há {} anos.'.format(anos,alistamento))
        print('Seu alistamento será no ano de {}.'.format(ano_atual + alistamento))
    else:
        print('Você tem/terá {} anos este ano. É hora de se alistar!'.format(anos))
except ValueError:
    print('Ano inválido!')