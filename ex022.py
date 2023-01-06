nome = str(input('Digite seu nome: ')).strip()
dividido = nome.split()

print(f'{nome.upper()} com letras maiúsculas')
print(f'{nome.lower()} com letras minúsculas')
print('Seu tem ao todo {} letras sem considerar os espaços'.format(len(nome)-nome.count(' ')))
print(f'{dividido[0]} tem {len(dividido[0])} letras')