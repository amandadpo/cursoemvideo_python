def soma(a,b):
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

def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(2,4)
soma(9,2,3,4)
