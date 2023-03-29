try:    
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Dados informados são inválidos!')
except ZeroDivisionError:
    print('Não existe divisão por zero')
except KeyboardInterrupt:
    print('Usuário preferiu não informar os dados.')
except Exception as erro:
    print(f'O erro encontrado foi {erro}') #apenas quando está desenvolvendo para verificar um possível erro no programa para poder tratá-lo
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre!')
