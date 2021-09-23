
# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# – EQUILÁTERO: todos os lados iguais

# – ISÓSCELES: dois lados iguais, um diferente

# – ESCALENO: todos os lados diferentes


x= int(input('Digite um lado: '))
y= int(input('Digite um lado: '))
z= int(input('Digite um lado: '))

if x == y == z:
  print('EQUILÁTERO: todos os lados iguais')
elif x == y != z or x != y == z or x == z != y:
  print('ISÓSCELES: dois lados iguais, um diferente')
elif x != y != z:
  print('ESCALENO: todos os lados diferentes')