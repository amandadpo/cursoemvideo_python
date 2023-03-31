t1 = 0
t2 = 1
lista_fibonacci = [0,1]

print('Sequência de Fibonacci')
print('-' * 35)
while True:
    try:
        n = int(input('Quantos números você quer mostrar? '))
        break
    except (ValueError, TypeError):
        print('Erro! Digite apenas números.')
    except KeyboardInterrupt:
        print('Entrada de dados interrompida pelo usuário.')

while True:
    try:
        x = int(input('Digite um número para ver se pertence a sequência informada: '))
        break
    except (ValueError, TypeError):
        print('Erro! Digite apenas números.')
    except KeyboardInterrupt:
        print('Entrada de dados interrompida pelo usuário.')
    
print('-' * 35)
print('Sequência solicitada:')
print(f'{t1} -> {t2}', end='')
cont = 3

while cont <= n:
    t3 = t1 + t2
    print(f' -> {t3}',end='')
    t1 = t2
    t2 = t3
    cont += 1
    lista_fibonacci.append(t3)
print(' -> FIM')

for i in lista_fibonacci:
    if x in lista_fibonacci:
        print(f'O número {x} pertence a Sequência de Fibonacci informada.')
        break
    else:
        print(f'O número {x} \033[0;31mNÂO\033[m pertence a Sequência de Fibonacci informada.')
        break
