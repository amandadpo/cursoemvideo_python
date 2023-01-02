real = float(input("Digite quanto possui em reais: "))
dolar = real / 5.26
euro = real / 5.58
print('Você possui R$ {:.2f} que podem ser convertidos para US$ {:.2f} e {:.2f} euros'.format(real,dolar,euro))