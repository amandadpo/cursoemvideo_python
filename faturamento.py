import json
x = []
cont = 0

with open("dados.json") as meu_json:
    dados = json.load(meu_json)

for k,v in enumerate(dados):
    x.append(v['valor'])

print(f'O maior valor de faturamento é {max(x)}')
print(f'O menor valor de faturamento {min(x)}')
    
media = sum(x) / (len(x) - x.count(0))

for c in x:
    if c > media:
        cont += 1

print(f'{cont} dias no mês em que o valor de faturamento diário foi superior à média mensal {media:.2f} ')