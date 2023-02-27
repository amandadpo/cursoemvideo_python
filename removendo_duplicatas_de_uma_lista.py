'''compras = ['sabonete','sabão em pó','leite','pão','açúcar','leite','sabonete']

print(compras)

lista = []
    
for i in compras:
    if i not in lista:
        lista.append(i)
        print(f'Item {i} adicionado')
    else:
        print(f'Item {i} duplicado. Será removido.')
    
                      
print(lista)'''

lista =  []
print('-='*5,'LISTA DE COMPRAS','-='*5)
while True:

    compras = str(input('Itens das compras: '))
    lista.append(compras)
    
    lista_completa = []
    
    resp = str(input('Inserir outro item [S/N]: ')).upper().strip()[0]
    if resp in 'N':
        print('Fim da lista.')
        break

for i in lista:
        if i not in lista_completa:
            lista_completa.append(i)
        else:
            print(f'Item {i} duplicado.')    

print(f'Lista de compras: {lista_completa}')





