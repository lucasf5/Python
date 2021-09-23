from random import randint
from operator import itemgetter

# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

dados = {'Jogador 1': randint(1,6),
'Jogador 2': randint(1,6),
'Jogador 3': randint(1,6),
'Jogador 4': randint(1,6),}


print('Valores Sorteados')
for k,c in dados.items():
  print(f'{k} tirou {c} no dado.')

dados = sorted(dados.items(), key=itemgetter(1), reverse=True)

for i,c in enumerate(dados):
  print(f'Posição {i+1}: O jogador {c[0]} tirou {c[1]} no dado.')

