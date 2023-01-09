cidade = str(input('Cidade onde nasceu: ')).upper().split()  
try:
    print('SANTO' in cidade[0])
except IndexError:
    print('Digite uma cidade válida')




