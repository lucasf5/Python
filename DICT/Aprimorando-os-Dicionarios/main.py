# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogo = dict()
partidas = []
registro = []
inicial = 10
while True:
  print('======CADASTRO======')
  count = 0
  jogo['nome']=str(input('NOME: ')).upper()
  print('======PARTIDAS======')
  jogo['partidas']=int(input('Partidas jogadas: '))
  for i in range(0,jogo['partidas']):
    count +=1

    jogo['golspartidas']=int(input(f'Quantos gols na partida {count}: '))
    partidas.append(jogo['golspartidas'])
  registro.append(jogo.copy())
  x = str(input('Deseja cadastrar outro jogador? [s/n]')).lower()
  if x == 'n':
    break
print('======DADOS======')
print(registro)

for c in registro:
  print('======REGISTRO======')
  print(f"Jogador: {c['nome']}")
  print(f"Jogou: {c['partidas']} partidas.")
  print('======PARTIDAS======')
  for x,i in enumerate(partidas):
    print(f'Na partida {x+1} fez {i} gols.')

# print('======PARTIDAS======')
# for i,x in enumerate(partidas):
#   print(f"Na partida {i+1} o jogador {c['nome']} fez {x}")


