# Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

N = int(input('Digite um numero: '))
count = 0
lista = []

while N < 999:
  lista.append(N)
  count +=1
  N = int(input('Digite um numero: '))

media = (sum(lista)/len(lista))
print(f'A media é: {media}')

print(f'A contagem dessa lista foi: {len(lista)}')
print(f'O maior numero dessa lista foi: {max(lista)}')
print(f'O menor numero dessa lista foi: {min(lista)}')