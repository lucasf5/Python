# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

x = int(input('Digite um numero: '))
print(f'O numero digitado é: {x}')
total = 0

for i in range(1,x+1):
  if x % i == 0:
    print('\033[34m')
    total += 1
  else:
    print('\033[31m')
  print(f'{i}', end=' ')

print(f'\nO numero {x} foi divisivel {total} vezes')
if total == 2:
  print('É primo!')
elif total > 2:
  print('Não é primo!')