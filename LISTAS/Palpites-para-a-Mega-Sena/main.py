import random
# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
lista = []
y = int(input('Quantos programas você quer? '))
count = 0
for i in range(0,y):
  i = random.choices(range(1,60), k=6)
  lista.append(i)
  count+=1
  print('='*30)
  print(f'O jogo {count} é: {i}')


