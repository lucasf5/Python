import math
# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

# 5! = 5 x 4 x 3 x 2 x 1 = 120

x = int(input('Digite o numero: '))
resul = math.factorial(x)

while x > 0:
  print(f'{x}', end='')
  print(' x ' if x > 1 else f' = {resul}', end='')
  x -= 1
  
