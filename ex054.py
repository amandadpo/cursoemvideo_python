from datetime import date
ano_atual = date.today().year
cont_maior = cont_menor = 0

try:
    for c in range(1,8):
        ano_nascimento = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
        if ano_nascimento < 0:
            print('Informe um ano válido.')
            break
        idade = ano_atual - ano_nascimento
        if idade >= 18:
            cont_maior += 1   
        else:
            cont_menor +=1
except ValueError:
    print('Dados inválidos.')
        
print(f'{cont_maior} pessoas são maiores de idade')
print(f'{cont_menor} pessoas são menores de idade')