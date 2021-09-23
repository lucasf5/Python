# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.


def ficha(Nome= 'Desconhecido', Gols = 0):
  print(f'O nome é {Nome} e fez {Gols} gols.')

ficha(Gols = 5)