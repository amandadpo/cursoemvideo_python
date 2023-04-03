import msg
import arquivo

arq = 'cursoemvideo.txt'

if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)
msg.cabeçalho('MENU PRINCIPAL')

while True:
    try:
        opc = int(input('Sua opção: '))
        break
    except (ValueError,TypeError):
        print('\033[31mERRO: Digite uma opção válida.\033[m')
    except KeyboardInterrupt:
        print('\033[31mOperação cancelada pelo usuário.\033[m')
     
if opc == 1:
    print('-' * 42)
    arquivo.lerArquivo(arq)
elif opc == 2:
    print('-' * 42)
    print('NOVO CADASTRO')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    arquivo.cadastrar(arq,nome,idade)
elif opc == 3:
    print('-' * 42)
    print('Saindo do sistema... Até logo!')
else:
    print('-' * 42)
    print('OPÇÃO INVÁLIDA'.center(42))
        
