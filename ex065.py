cont = 0
soma = 0 
numero = 0
pergunta = 'S'
maior = menor = 0

while pergunta in 'S':
    numero = int(input('Digite um número inteiro: '))
    pergunta = str(input('Deseja continuar [S]im/[N]ão: ')).upper().strip()
    cont += 1
    soma += numero
    media = soma / cont

    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

print('Foram exibidos {} números e a média entre eles é {:.2f}'.format(cont,media))
print('O menor número é {} e o maior número é {}'.format(menor,maior))