from math import radians,sin,cos,tan
angulo = float(input('Digite o ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}, o COSSENO de {:.2f} e a tangente de {:.2f}'.format(angulo, seno,cosseno,tangente))
