def ajuda(a):
    from time import sleep
    sleep(1)
    print('=' * 27)
    print(f'\033[1;36mAcessando o comando "{n}"\033[m')
    print('-' * 27)
    sleep(2)
    help(a)

    return a

print('-' * 30)
print('\033[1;34;40m  SISTEMA DE AJUDA PYHELP\033[m')
print('-' * 30)

while True:
    n = str(input('Função ou biblioteca: '))
    if n.upper() == 'FIM':
        print('^' * 12)
        print('\033[1;35m Até logo!\033[m')
        break
    else:
        ajuda(n)