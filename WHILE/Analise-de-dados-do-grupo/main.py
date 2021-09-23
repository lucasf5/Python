# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

# A) quantas pessoas tem mais de 18 anos.

# B) quantos homens foram cadastrados.

# C) quantas mulheres tem menos de 20 anos.

S = int(input('Sexo [0] M ou [1] F: '))
I = int(input('Qual a idade: '))

H = []
M = []
MM20 = []
ID18 = []

A = 0

while A != 1:
  if I > 18:
    ID18.append(I)
  if S == 0:
    H.append(I)
  if S == 1:
    M.append(I)
  if S == 1 and I < 20:
    MM20.append(I)
  S = int(input('Sexo [0] M ou [1] F: '))
  I = int(input('Qual a idade: '))
  A = int(input('Deseja continuar: N/S: '))

x = len(H)
print(f'O numero de homens é {x}')

y = len(M)
print(f'O numero de mulheres é {y}')

z = len(MM20)
print(f'O numero de mulheres com menos de 20 anos é: {z}')

w = len(ID18)
print(f'O numero de pessoas com mais de 18 anos é: {w} ')
