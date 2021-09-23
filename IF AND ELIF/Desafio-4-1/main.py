# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

x = int(input('Digite sua idade: '))

if x == 18:
  print('Você irá se alistar esse ano!')
elif x > 18:
  print('Já passou o tempo do tempo de se alistar!')
  y = x - 18
  print(f'Já se passou {y} anos!')
elif x < 18:
  print('Já passou o tempo do tempo de se alistar!')
  y = 18 - x
  print(f'Falta {y} anos para se alistar!')