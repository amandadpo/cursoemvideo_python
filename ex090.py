situacao_aluno = {}
situacao_aluno['Nome'] = str(input('Nome do aluno: '))
situacao_aluno['Média']= float(input(f'Média de {situacao_aluno["Nome"]}: '))

if situacao_aluno['Média'] >= 7:
    situacao_aluno['Situação'] = "APROVADO"
elif  5 <=  situacao_aluno['Média'] < 7:
    situacao_aluno['Situação'] = "RECUPERAÇÂO"
else:
    situacao_aluno['Média'] = "REPROVADO"

print('-='*30)
for k,v in situacao_aluno.items():
    print(f'- {k} = {v}')
    

