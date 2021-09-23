# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista = []
x = 0
while x != 999:
  lista.append(x)
  x = int(input('Digite um numero: '))


lista = set(lista)
lista = sorted(lista)
lista = list(lista)
print(lista)