# Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area():
  x = int(input('Digite a largura: '))
  y = int(input('Digite o comprimento: '))
  Area = x*y
  print(f'A area do terreno é {Area} m^2')

area()