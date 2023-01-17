try:
    numero = int(input("Digite um número inteiro: "))
    escolha = int(input("""[ 1 ] Converter para BINÁRIO \n[ 2 ] Converter para OCTAL \n[ 3 ] Converter para HEXADECIMAL \nEscolha a base de conversão: """))
    if escolha == 1:
        print('{} convertido para BINÁRIO é {}'.format(numero,bin(numero)))
    elif escolha == 2:
        print('{} convertido para OCTAL é {}'.format(numero,oct(numero)))
    elif escolha == 3:
        print('{} convertido para BINÁRIO é {}'.format(numero,hex(numero)))
    else:
        print('Digite uma opção válida.')
except ValueError:
    print('Digite apenas números inteiros')