n = input("Digite algo: ")
tipo = type(n) 
print(f"O tipo primitivo de {n} é {tipo}")
print("Só tem espaços? ", n.isspace())
print("É numero? ", n.isnumeric())
print("É alfabético? ", n.isalpha())
print('É alfanumérico? ', n.isalnum())
print('É toda maiúscula? ', n.isupper())
print('É toda minúscula? ', n.islower())
print('Está capitalizada? ', n.istitle())
