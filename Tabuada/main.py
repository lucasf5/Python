# Exercício Python 9: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

x = int(input('Digite o numero: '))

print(f'{x}*0 = {x*0}')
print(f'{x}*1 = {x*1}')
print(f'{x}*2 = {x*2}')
print(f'{x}*3 = {x*3}')
print(f'{x}*4 = {x*4}')
print(f'{x}*5 = {x*5}')
print(f'{x}*6 = {x*6}')
print(f'{x}*7 = {x*7}')
print(f'{x}*8 = {x*8}')
print(f'{x}*9 = {x*9}')
print(f'{x}*9 = {x*10}')

# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

for i in range(0,11):
  print(f'{x}*{i} = {x*i}')
