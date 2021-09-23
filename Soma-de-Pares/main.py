# Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
lista = []
for i in range(1,7):
  a=int(input('Digite um numero: '))
  if a % 2 ==0:
    lista.append(a)

print(sum(lista))