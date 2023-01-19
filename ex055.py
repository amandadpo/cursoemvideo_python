peso_maior = peso_menor = 0

try:
    for c in range(1,6):
        peso = float(input(f'Informe o peso da {c}ª pessoa: '))
        if peso <= 0:
            print('Digite um peso válido.')
            break
        if c == 1:
            peso_maior = peso
            peso_menor = peso
        else:
            if peso > peso_maior:
                peso_maior = peso
            if peso < peso_menor:
                peso_menor = peso

except ValueError:
    print('Dados inválidos.')

print(f'O menor peso lido foi {peso_menor} kg')
print(f'O maior peso lido foi {peso_maior} kg')