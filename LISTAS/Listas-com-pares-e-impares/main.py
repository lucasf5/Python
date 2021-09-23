# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista = []
listapar = []
listaimpar = []

for i in range(0,7):
  x = int(input('Digite um numero: '))
  if x%2==0:
    listapar.append(x)
  else:
    listaimpar.append(x)
  
listaimpar.sort()
lista.append(listaimpar[:])
listapar.sort()
lista.append(listapar[:])
print(lista)