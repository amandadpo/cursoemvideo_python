from datetime import date
ano_atual = date.today().year
funcionario = {}
funcionario['Nome'] = str(input('Nome: '))
funcionario['Idade'] = int(input('Ano de Nascimento: '))
funcionario['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if funcionario['CTPS'] > 0:
    funcionario['Ano de contratação'] = int(input('Ano de contratação: '))
    funcionario['Salário'] = float(input('Salário R$ '))
    funcionario['Ano de aposentadoria'] = funcionario['Ano de contratação'] + 35
    funcionario['Idade de aposentadoria'] = funcionario['Ano de aposentadoria'] - funcionario['Idade']

funcionario['Idade'] = ano_atual - funcionario['Idade']
print('='*40)
for k,v in funcionario.items():
    print(f'{k} = {v}')
