# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.                  
# Depois disso, mostre:                                                                                                                                       
# A) Quantos números foram digitados.                                                                                                                    
# B) A lista de valores, ordenada de forma decrescente.                                                                                          
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
x = 0
while True:
  x = int(input('Digite: '))
  if x == 999:
    break
  lista.append(x)

print(f'Foram digitados {len(lista)}')
lista.sort()
print(f'Numeros digitados decrescente: {lista[::-1]}')
if 5 in lista:
  print(f'O 5 foi digitado e está na posição {lista.index(5)}')
else:
  print('5 não foi digitado!')
