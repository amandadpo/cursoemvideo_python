def linha(tamanho = 42):
    return '-' * tamanho

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
    print("""1 - Ver pessoas cadastradas
2 - Cadastrar novas pessoas
3 - Sair do sistema""")

