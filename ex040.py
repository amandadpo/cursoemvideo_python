try: 
    nome_aluno = str(input('Digite o nome do aluno: '))
    nota_1 = float(input('Digite a primeira nota: '))
    nota_2 = float(input('Digite a segunda nota: '))

    media = (nota_1 + nota_2) / 2

    if media < 5:
        print(f'{nome_aluno} sua média é {media:.2f}. Você está REPROVADO!')
    elif media > 5 and media <= 6.9:
        print(f'{nome_aluno} sua média é {media:.2f}. Você está de RECUPERAÇÂO!')
    else:
        print(f'{nome_aluno} sua média é {media:.2f}. Você está APROVADO!')
except ValueError:
    print('Dados inválidos!')