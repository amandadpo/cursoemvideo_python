from time import sleep

def contador(inicio,fim,passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('=-'*20)
    print(f'Contagem de {inicio} a {fim} de {passo} em {passo}:')
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(cont, end=' ')
            sleep(0.5)
            cont += passo
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            print(cont, end=' ')
            sleep(0.5)
            cont -= passo
        print('FIM')

#contador(1,10,1)
#contador(10,0,2)
print('=-'*20)
print('Sua vez!')
i = int(input('Informe o início: '))
f = int(input('Informe o fim: '))
p = int(input('Informe o passo: '))
contador(i,f,p)