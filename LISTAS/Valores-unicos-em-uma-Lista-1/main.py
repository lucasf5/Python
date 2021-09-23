lista = []
x = 0
while x != 999:
  x = int(input('Numero: '))
  if x not in lista:
    lista.append(x)


lista.sort()
print(lista)

  