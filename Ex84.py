# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre:                                                                                                    
# A) Quantas pessoas foram cadastradas.                                                                                                                
# B) Uma listagem com as pessoas mais pesadas.                                                                                                    
# C) Uma listagem com as pessoas mais leves.

dado = []
registro = []
totalpesado = 0
totalleve = 0

for i in range(0,5):
  dado.append(str(input('Nome: ')))
  dado.append(int(input('Peso: ')))

  registro.append(dado[:])
  dado.clear()

for i in registro:
  if i[1] >= 90:
    print(f'{i[0]} é pesado e possui {i[1]} kgs')
    totalpesado+=1
  elif i[1] < 90: 
    print(f'{i[0]} é leve e possui {i[1]} kgs ')
    totalleve+=1

print(f'Temos um total de {totalpesado} pessoas pesadas e um total de {totalleve} de pessoas leves.')