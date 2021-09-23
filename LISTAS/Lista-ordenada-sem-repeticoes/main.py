# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
lista = []
for i in range(1,6):
  x = input('Numero: ')
  lista.append(x)

lista.sort()
print(lista)

