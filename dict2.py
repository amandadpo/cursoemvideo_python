nome_time = {'Amanda':'Vasco','Alessandro':'Flamengo','Ragnar':'Barcelona'}
print(nome_time['Alessandro'])
print(nome_time['Amanda'])
print(nome_time['Ragnar'])

print('=' * 30)
chave = 'Ragnar'
#print(nome_time[chave])
print(nome_time.get(chave,'Nenhum time encontrado'))

print('=' * 30)
chaves = ['Amanda','Alessandro','Ragnar']
print(nome_time[chaves[0]])
print(chaves)
print(chaves[0]) #chaves[0] == Amanda
print(chaves[1]) #chaves[1] == Alessandro
print(chaves[2]) #chaves[2] == Ragnar

print('=' * 30)
chaves_nome_time = list(nome_time.keys())

print(chaves_nome_time[0]) #chaves[0] == Amanda
print(nome_time[chaves_nome_time[0]])
print(chaves_nome_time[1]) #chaves[1] == Alessandro
print(chaves_nome_time[2]) #chaves[2] == Ragnar

#chaves_nome_time = banco_dados.get_all()

for key in chaves_nome_time:
    print(nome_time[key])


print('=' * 30)
pessoas = {
    'Amanda':{
        'Idade':'31',
        'Sexo':'Feminino',
        'Time':'Vasco',
        'Cidade':'Rio de Janeiro'
    },
    'Alessandro':{
        'Idade':'31',
        'Sexo':'Feminino',
        'Time':'Flamengo',
        'Cidade':'Rio de Janeiro'
    },
    'Ragnar':{
        'Idade':'2',
        'Sexo':'Macho',
        'Time':'Fluminense',
        'Cidade':'Rio de Janeiro'
    }
}

print('-' * 50)
print(pessoas) #imprimir o dicionário


print('-' * 50)
print(pessoas['Amanda'])


print('-' * 50)
print(pessoas.keys()) #mostrar a chave 

print('-' * 50)
print(pessoas.values()) #mostra os valores

print('-' * 50)
print(pessoas.items()) #mostra o dicionário

print('-' * 50)
print(pessoas.get('Amanda')) #mostra os valores da Amanda

print('-' * 50)
lista_pessoas = list(pessoas)
print(lista_pessoas) #mostrar a chave em uma lista (nome das pessoas)


print(lista_pessoas[0])
print(lista_pessoas[1])
print(lista_pessoas[2])

print('-' * 50)
for c in pessoas: 
    print(pessoas[c]) #mostrar o conteúdo

print('-' * 50)
for c in pessoas: 
    print(pessoas[c]['Idade']) #mostrar a idade

print('-' * 50)
for c in pessoas: 
    print(pessoas[c]['Sexo']) #mostrar o sexo

print('-' * 50)
for c in pessoas:
    print(pessoas[c]['Time']) #mostrar o time
print('-' * 50)
for c in pessoas:
    print('Nome: ', end='')
    print(c)
    print('Cidade: ', end='')
    print(pessoas[c]['Cidade']) 





