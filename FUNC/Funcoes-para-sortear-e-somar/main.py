import random
# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

numeros = []
soma = []

def sorteia():
  numeros.append(random.choices(range(0,100), k=5))
  print(numeros[0])

def somaPar():
  for i in numeros:
   print(f'Os numeros escolhidos são: {i}')
   for x in i:
     if x%2==0:
      soma.append(x)

  print(f'Os numeros pares são: {soma}')
  x = sum(soma)
  print(f'{x}')

sorteia()
somaPar()