from time import sleep
# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada: 

# a) de 1 até 10, de 1 em 1 
# b) de 10 até 0, de 2 em 2 
# c) uma contagem personalizada


def contador():
  for i in range(0,11):
    print(i, end=' ', flush=True)
    sleep(0.5)
  print('\n')
  for x in range(10,0,-2):
    print(x, end=' ', flush=True)
    sleep(0.5)
  print('\n')
  a = int(input('Digite o numero que quer iniciar: '))
  b = int(input('Digite o numero que quer terminar: '))
  c = int(input('De quantos em quantos até chegar: '))

  for x in range(a,b,c):
    print(x, end=' ', flush=True)
    sleep(0.5)

contador()