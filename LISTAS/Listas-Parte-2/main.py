lista = [['lucas', 25], ['pedro', 50], ['yan', 19]]

print(lista[0])
print(lista[0][0])
print(lista[0][1])

pessoas = []
pessoas.append('Victor')
pessoas.append(10)

lista.append(pessoas[:])
print(lista)


for i in lista:
  print(f'{i[0]} tem {i[1]} anos de idade')


registro = []
dado = []
totmaior = 0
totmenor = 0

for i in range(0,3):
  dado.append(str(input('Nome: ')))
  dado.append(int(input('idade: ')))
  registro.append(dado[:])
  dado.clear()

for i in registro:
  if i[1] >=21:
    print(f'{i[0]} é maior de idade')
    totmaior += 1
  else:
    print(f'{i[0]} é menor de idade')
    totmenor += 1

print(f'Temos {totmaior} maiores e {totmenor} menores.')