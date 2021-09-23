# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

valor = int(input('Quanto quer sacar? R$ '))
ced = 50
totalced = 0
count1 = 0

count50 = 0
count20 = 0
count10 = 0
count1 = 0

while True:
  if valor >= ced:
    valor -= ced
    totalced += 1
  else:
    print(f'Total de {totalced} cédulas de R$ {ced}')
    if ced == 50:
      ced = 20
    elif ced == 20:
      ced = 10
    elif ced == 10:
      ced = 1
    totalced = 0
    if valor == 0:
      break



print('Acabou!')