ficha = list()
while True:
    nome = str(input('Nome do aluno: '))
    nota1 = float(input('Nota 1:'))
    nota2 = float(input('Nota 2:'))
    media = (nota1 + nota2) / 2
    ficha.append([nome,[nota1,nota2],[media]])
    
    resp = str(input('Deseja continuar [S/N]: ')).strip().upper()
    if resp in 'N':
        break
print('-='*30)
print(f'{"Nº":<4}{"Nome":<10}{"Média":>6}')
print('-='*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]}')

while True:
    print('-='*30)
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opcao == 999:
        print('Finalizando...')
        break
    if opcao <= len(ficha)-1:
        print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}')
    