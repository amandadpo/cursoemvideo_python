medida = float(input('Digite a medida em metros(m): '))
dm = medida * 10
cm = medida * 100
mm = medida * 1000
dam = medida / 10
hm = medida / 100
km = medida / 1000
print('A medida de {:.2f} m corresponde a {:.2f} cm e {:.2f} mm'.format(medida,cm,mm))
