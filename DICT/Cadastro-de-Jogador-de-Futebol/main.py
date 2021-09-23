# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogo = dict()

jogo['nome']=str(input('NOME: '))
jogo['golsfeitos']=int(input('GOLS: '))
jogo['golspartidas']=int(input('PARTIDA: '))

for c,v in jogo.items():
  print(f'{c} -> {v}')

print(f'O jogador fez: {jogo["golspartidas"] - jogo["golsfeitos"]} gols')