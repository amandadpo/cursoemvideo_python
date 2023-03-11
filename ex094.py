cadastro = {}
lista = []
total_idade = []
mulheres = []
maiores = []

while True:
    cadastro['Nome'] = str(input('Nome: '))

    while True:
        cadastro['Sexo'] = str(input('Sexo [F/M]: ')).upper()

        if cadastro['Sexo'] in 'MF':
            break
        print('Por favor digite apenas F ou M.')

    if cadastro['Sexo'] == 'F':
        mulheres.append(cadastro['Nome'])
     
    while True:
        try: 
            cadastro['Idade'] = int(input('Idade: '))
        except ValueError:
            print('Dígito inválido.')
            continue
        total_idade.append(cadastro['Idade'])

        if cadastro['Idade'] > 0:
            break
        print('Idade inválida!')
            
    lista.append(cadastro.copy())

    while True:
        resposta = str(input('Deseja continuar [S/N]: ')).upper().strip()
        if resposta in 'SN':
            break
        print('Por favor digite apenas S ou N.')
    if resposta == 'N':
        break

print('-='*30)
print(f'A) Foram cadastradas {len(lista)} pessoas.')

media = sum(total_idade) / len(lista)
print(f'B) Média de idade do grupo: {media:.2f} anos.')

print('C) As mulheres são:',end=' ')
for c in mulheres:
    print(c, end=' ')
print()

print('D) Lista das pessoas que estão com idade acima da média: ',end=' ')
print()
for c in lista:
    if c['Idade'] > media:
        for k, v in c.items():
            print(f'{k} = {v}; ', end=' ')
        print()
print('<< ENCERRADO >>')
    






