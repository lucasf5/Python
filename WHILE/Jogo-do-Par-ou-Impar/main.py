import random
# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

n = int(input('[0] Par ou [1] Impar?: '))
x = random.randint(0,1)
count = 0

while x == n:
  print(f'O computador escolheu: {x}\n Você escolheu: {n}')
  print('Você venceu!')
  count += 1
  x = random.randint(0,1)
  n = int(input('[0] Par ou [1] Impar?: '))


print('Você perdeu!')
print(f'O numero de vitórias foi: {count}')