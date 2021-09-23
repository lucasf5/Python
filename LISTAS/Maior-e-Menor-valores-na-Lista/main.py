import random
# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

x = random.choices(range(1,10), k=5)
print(f'A lista é: {x}')

print(f'O maior valor é: {max(x)} e está na posição {x.index(max(x))}')
print(f'O menor valor é: {min(x)} e está na posição {x.index(min(x))}')