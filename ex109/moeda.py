def metade(n=0, formatado = False):
    m = n/2
    return m if formatado is False else moeda(m)

def dobro(n = 0, formatado = False):
    d = n * 2
    return d if formatado is False else moeda(d)

def aumentar(n = 0, formatado = False):
    a = (n * 0.1) + n
    return a if formatado is False else moeda(a)

def diminuir(n = 0, formatado = False):
    r = n - (n * 0.13)
    return r if formatado is False else moeda(r)

def moeda(preço = 0, moeda = "R$"):
    return f'{moeda} {preço:>.2f}'.replace('.',',')