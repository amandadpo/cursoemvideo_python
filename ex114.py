import urllib
import urllib.request
try:
    site = urllib.request.urlopen('https://www.google.com.br/')
except urllib.error.URLError:
    print('Não consegui acessar o site do GOOGLE nesse computador.')
else:
    print('GOOGLE acessado com sucesso!')
    print(site.read())