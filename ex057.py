sexo = str(input('Sexo [F]/[M]: ')).strip().upper()[0]
while sexo not in 'MF':
    print('Sexo inválido. Digite M ou F.')
    sexo = str(input('Sexo [F]/[M]: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado.')
