sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53
soma = sp + rj + mg + es + outros
sp_percent = (sp / soma) * 100
rj_percent = (rj / soma) * 100
mg_percent = (mg / soma) * 100
es_percent = (es / soma) * 100
outros_percent = (outros / soma) * 100
print(' - - Percentual dos estados - -')
print(f'São Paulo = {sp_percent:.2f}%')
print(f'Rio de Janeiro = {rj_percent:.2f}%')
print(f'Minas Gerais = {mg_percent:.2f}%')
print(f'Espírito Santo = {es_percent:.2f}%')
print(f'Outros = {outros_percent:.2f}%')