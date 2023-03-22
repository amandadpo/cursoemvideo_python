def fatorial(num,show=True):
    print(f'{num}! = ',end="")
    f = 1
    for c in range(num,0,-1):
        if show == True:
            print(f'{c} ',end="")
            if c > 1:
                print('x ' , end="")
            else:
                print('= ' , end="")
        f *= c
    return f

num = int(input('Digite um número para ver o fatorial: '))
print(fatorial(num,False))


