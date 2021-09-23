# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

N = int(input('Numero: '))
lista = []
count = 0

while N < 999:
  lista.append(N)
  N = int(input('Numero: '))
  count += 1

print(f'Foi colocado {count} itens na lista.')
x = sum(lista)
print(f'A soma de todos eles é: {x}')
