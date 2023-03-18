'''def soma(a,b):
    s = a + b
    print(s)

#Programa principal
soma(4,5)
soma(3,2)
soma(9,3)

def soma(a,b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')

soma(b=4,a=5)
soma(7,2)

def contador(*num):
    tamanho = len(num)
    print(f'Recebi os valores {num} e são ao todo {tamanho}')

contador(2,1,4)
contador(0,8)
contador(1,2,3,4,5,6,7,9)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [2,8,3,1,5]
dobra(valores)
print(valores)

def soma(*valores): # múltiplos parâmetros
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(2,4)
soma(9,2,3,4)'''

help(print) 

#docstrings
def contador(i,f,p):
    """ 
    Faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p    
    print('FIM!')

help(contador)


def soma(a=0,b=0,c=0):  # Parâmetros opcionais
    """
     Faz a soma de três valores e mostra o resultado na tela
    :param a: o primeiro valor 
    :param b: o segundo valor
    :param c: o terceiro valor
    """
    s = a+b+c
    print(f'A soma vale {s}')

soma(1,2,3)
soma(1,2)
soma(1)
soma()
soma(b=4,c=2)
print()

# Escopo de varáveis (local onde a variável vai existir/deixar de existir)
def teste(b):
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')
print()

def teste(b):
    a = 8   # local
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5  #global
teste(a)
print(f'A fora vale {a}')   
print()

def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')
print()

def soma(a=0,b=0,c=0):
    s = a + b + c
    return s

r1 = soma(2,3,4)
r2 = soma(5,6)
r3 = soma(1)
print(f'As somas dos resultados foram: {r1}, {r2} e {r3}')
print()

def fatorial(num):
    f = 1
    for c in range(num,0,-1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial(0)
print(f'Os resultados dos fatoriais são: {f1}, {f2} e {f3}')
print()
n = int(input('Digite um número: '))
print(f'O fatorial de {n} é {fatorial(n)}.')
print()

def Par(num=0):
    if num % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
print(Par(num))
if Par(num):
    print('É par!')
else:
    print('É ímpar!')