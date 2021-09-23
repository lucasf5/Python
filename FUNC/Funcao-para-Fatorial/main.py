import math
# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(calcular, show=True):
  x = math.factorial(calcular)
  if show == True:
    while calcular != 1:
      print(f'{calcular}', end=' x ')
      calcular-=1
      if calcular == 1:
        print('1 = ', end='')
  print(x)


fatorial(18)