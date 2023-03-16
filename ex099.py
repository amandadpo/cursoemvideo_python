def maior(* valores):
    contador = maiornum = 0
    print(f'Foram informados {len(valores)} valores.')
    for n in valores:
        if contador == 0:
            maiornum = n
        else:
            if n > maiornum:
                maiornum = n
        contador += 1

    print(f'Foram informados os valores: {valores} e o maior número encontrado foi {maiornum} .')
    print('=' * 70)

maior(1,2,3)
maior(1,2,3,4,5,6,7)
maior(2,9,7,10,8)
maior(5)
maior()

