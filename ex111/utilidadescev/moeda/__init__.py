def metade(n=0, formatado = False):
    m = n/2
    return m if formatado is False else moeda(m)

def dobro(n = 0, formatado = False):
    d = n * 2
    return d if formatado is False else moeda(d)

def aumentar(n = 0,taxa=0, formatado = False):
    a = (n * taxa) + n
    return a if formatado is False else moeda(a)

def diminuir(n = 0,taxa=0, formatado = False):
    r = n - (n * taxa)
    return r if formatado is False else moeda(r)

def moeda(preço = 0, moeda = "R$"):
    return f'{moeda} {preço:>.2f}'.replace('.',',')

def resumo(p=0,txaumento=10,txreducao=5):
    print('-' * 35)
    print('Resumo do valor'.center(35))
    print('-' * 35)
    print(f'Preço analisado:\t{moeda(p)}')
    print(f'Dobro do preço:\t\t{dobro(p,True)}')
    print(f'Metade do preço:\t{metade(p,True)}')
    print(f'{txaumento*100:.0f}% de aumento:\t\t{aumentar(p,txaumento,True)}')
    print(f'{txreducao*100:.0f}% de redução:\t\t{diminuir(p,txreducao,True)}')
    print('-' * 35)
