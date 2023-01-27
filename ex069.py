pessoas_maiores_18 = 0
homens = 0
mulheres_menos_20 = 0

print('=' * 40)
print('Cadastrando pessoas')
print('=' * 40)

while True:
    try:
        idade = int(input('Idade: '))
        if idade <= 0:
            print('Idade inválida')
            break

        if idade > 18:
            pessoas_maiores_18 += 1

        sexo = str(input('Sexo [F/M]: ')).upper().strip()[0]
        while sexo not in 'FM':
            sexo = str(input('Sexo [F/M]: ')).upper().strip()[0]

        if sexo == 'M':
            homens += 1
        elif sexo == 'F' and idade < 20:
            mulheres_menos_20 +=1

        opcao = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
        while opcao not in 'SN':
            opcao = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
        
        if opcao == 'N':
            print('Finalizando...')
            break
    except ValueError:
        print('Dados inválidos.')

print('=' * 40)
print(f'{pessoas_maiores_18} pessoas tem mais de 18 anos.')
print(f'Foram cadastrados {homens} homens.')
print(f'Foram cadastradas {mulheres_menos_20} mulheres com menos de 20 anos.')
    

    
