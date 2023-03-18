def voto(ano = 0):
    from datetime import date  
    idade = date.today().year - ano
    if idade < 16:
        return f'Você tem {idade} anos e você NÂO pode votar!'
    elif idade > 65 or idade < 18:
        return f'Você tem {idade} anos e seu VOTO é OPCIONAL!'
    else:
        return f'Você tem {idade} anos e seu VOTO é OBRIGATÓRIO!'
    
x = int(input('Em que ano você nasceu? '))
voto(x)
