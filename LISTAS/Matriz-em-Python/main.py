# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

lista = []
linha1 = []
linha2 = []
linha3 = []
counta = 0
countb = 0
countc = 0
pares = []

for i in range(0,3):
  a = int(input(f'Numero {[0,counta]}: '))
  counta+=1
  linha1.append(a)

for i in range(0,3):
  b = int(input(f'Numero {[1,countb]}: '))
  countb+=1
  linha2.append(b)

for i in range(0,3):
  c = int(input(f'Numero {[2,countc]}: '))
  countc+=1
  linha3.append(c)

lista.append(linha1[:])
lista.append(linha2[:])
lista.append(linha3[:])
print('='*30)
print(f'{linha1}\n{linha2}\n{linha3}')
print('='*30)
print(f'{lista[0]}\n{lista[1]}\n{lista[2]}')
print('='*30)

print([lista[0][0]], [lista[0][1]], [lista[0][2]])
print([lista[1][0]], [lista[1][1]], [lista[1][2]])
print([lista[2][0]], [lista[2][1]], [lista[2][2]])

print('='*30)
print(max(lista[1]))
print(sum(lista[2]))

for i in lista:
  for x in i:
    if x%2==0:
      pares.append(x)

print(sum(pares))