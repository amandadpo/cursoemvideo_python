soma = media = 0
homem_mais_velho = 0
nome_mais_velho =''
cont = 0

try:
    for c in range(1,5):
        print(f'----- {c} ª pessoa -----')
        nome = str(input(f'Nome: ')).strip().upper()

        idade = int(input('Idade: '))
        if idade <= 0:
            print('Idade inválida.')
            break
        else:
            soma += idade
            media = soma/c

        sexo = str(input('Sexo [F]/[M]: ')).upper().strip()[0]
        if sexo == 'M':
            if c == 1:
                homem_mais_velho = idade
                nome_mais_velho = nome
            if idade > homem_mais_velho:
                homem_mais_velho = idade
                nome_mais_velho = nome
        elif sexo == 'F':
            if idade < 20:
                cont += 1
        else:
            print('Digite F ou M.')
            break

except ValueError:
    print('Dados inválidos.')

print('A média de idade do grupo é {}'.format(media))
print('{} mulheres no grupo tem menos de 20 anos'.format(cont))
print('{} é o homem mais velho tem {} anos.'.format(nome_mais_velho.capitalize(),homem_mais_velho))
