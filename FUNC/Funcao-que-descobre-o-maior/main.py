# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
lista = []
def maior(*args):
  for i in args:
    lista.append(i)
  x = max(lista)
  print(lista)
  print(f'O maior numero digitado é: {x}')

maior(1,2,3,5,60,8,10,30,52,80,90,2050)