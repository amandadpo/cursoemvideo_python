numeros = ('zero','um', 'dois','três','quatro',
           'cinco','seis','sete','oito','nove',
           'dez','onze','doze','treze','quatorze',
           'quinze','dezesseis','dezessete','dezoito',
           'dezenove','vinte')
 
while True:
    numero = int(input('Digite um numero de 0 a 20: '))
    print('Você digitou:',numeros[numero])
    if numero < 0 or numero > 20:
        continue

    pergunta = str(input('Deseja continuar [S]/[N]: ')).upper().strip()[0]
    if pergunta in 'S':
        continue
    if pergunta in 'N':
        print('Encerrando programa...')
        break

