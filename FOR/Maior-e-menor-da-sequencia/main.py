# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

lista = []

for i in range(1,6):
  peso = float(input('Digite seu peso: '))
  lista.append(peso)

maximo = max(lista)
minimo = min(lista)

print(f'O maior peso é: {maximo}')
print(f'O menor peso é: {minimo}')