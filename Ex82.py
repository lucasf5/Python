# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
listapar = []
listaimpar = []

while True:
  x = int(input('Digite: '))
  if x == 999:
    break
  lista.append(x)

  if x%2==0:
    listapar.append(x)
  else:
    listaimpar.append(x)


lista.sort()
listapar.sort()
listaimpar.sort()

print(lista)
print(listapar)
print(listaimpar)