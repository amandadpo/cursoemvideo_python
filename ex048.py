soma = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        #print(c, end=' ')
        cont += 1
        soma += c
        
print(f' Existem {cont} números múltiplos de 3 no intervalo entre 1 e 500 e a soma deles é {soma}.')
