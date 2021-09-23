import urllib
import urllib.request

# Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

try:
  site = urllib.request.urlopen('http://www.pudim.com.br/')
except:
  print('Deu erro!')
else:
  print('Tudo ok!')