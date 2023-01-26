comida = {'banana','chocolate','sorvete'}
print(comida)
lista_comida = ['banana','chocolate','sorvete']
print(lista_comida[0])
comida_preferida_nome = {'Amanda':'Churrasco','Ragnar':'Qualquer coisa'}
print(comida_preferida_nome.get('alessandro'))
#del comida_preferida_nome['Amanda']    apagar do dicionário
print(comida_preferida_nome)

comida.add('churrasco')
print(comida)
comida_preferida_nome['Alessandro'] = 'macarrão'
print(comida_preferida_nome)

print(comida_preferida_nome.keys())

print('________________________________________')

for chave in comida_preferida_nome.keys(): #retorna a chave
    #print(comida_preferida_nome[chave])
    print(chave)

print('________________________________________')
for chave,valor in comida_preferida_nome.items(): # retorna keys e values 
    print(chave)
    print(valor)

print('________________________________________')
for valor in comida_preferida_nome.values():   #retorna os valores do dicionário
    print(valor)

print('________________________________________')
brasil = []
estado1 = {'uf':'Rio de Janeiro','sigla':'RJ'}
estado2 = {'uf':'São Paulo','sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

print('________________________________________')
estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('UF: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print('')