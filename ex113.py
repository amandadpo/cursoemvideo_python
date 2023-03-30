def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
            break
        except (ValueError, TypeError):
            print('\033[0;31mErro!Digite um número inteiro.\033[m')
        except KeyboardInterrupt:
            print('\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
    return n

def leiaFloat(msg2):
    while True:
        try:
            f = float(input(msg2))
            break
        except (ValueError, TypeError):
            print('\033[0;31mErro!Digite um número real.\033[m')
        except KeyboardInterrupt:
            print('\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
    return f  
    

num1 = leiaInt('Digite um nº inteiro: ')
num2 = leiaFloat('Digite um nº real: ')
print(f'Você digitou o número inteiro {num1} e o número real {num2}')

