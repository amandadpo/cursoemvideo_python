print('=' * 50)
print('{:^40}'.format('Banco Amandita'))
print('=' * 50)

print('Notas disponíveis: 100 - 50 - 20 - 10 - 5')
valor = int(input('Qual valor a ser sacado? '))
total = valor
cedula = 100
total_cedulas = 0

while True:
    if total >= cedula:
        total -= cedula
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'Total de {total_cedulas} cédulas de R$ {cedula}')
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5

        total_cedulas = 0
        if valor == 0:
            break
print('=' * 30)
print('Volte sempre. Tenha um bom dia!')






