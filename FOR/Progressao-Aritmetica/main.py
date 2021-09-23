# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

x = int(input('Valor: '))
y = int(input('Primeiro termo: '))
z = int(input('Segundo termo: '))
r = z-y


for i in range(1,10):
  a = x + (10 - 1)*r
  print(a)