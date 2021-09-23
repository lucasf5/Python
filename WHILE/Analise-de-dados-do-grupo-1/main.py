# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

# A) quantas pessoas tem mais de 18 anos.

# B) quantos homens foram cadastrados.

# C) quantas mulheres tem menos de 20 anos.

total18 = 0
menos20 = 0
Homens = 0
Mulheres = 0

while True:
  print('\033[7;33m------CADASTRO PESSOA------\033[m')
  idade = int(input('\033[7;30;43mIdade: \033[m'))
  sexo = ' '
  while sexo not in 'MF':
    sexo = str(input('\033[7;30;43mSexo: [M/F] \033[m')).strip().upper()
  if idade > 18:
    total18+=1

  if idade < 20 and sexo == 'F':
    menos20+=1

  if sexo == 'M':
    Homens+=1

  if sexo == 'F':
    Mulheres+=1


  resp = ' '
  while resp not in 'SN':
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
  if resp == 'N':
    break
print('Acabou!')

print(f'O total de mulheres com menos de 20 anos é: {menos20}')
print(f'O total de pessoas com mais de 18 anos é: {total18}')

print(f'O total de Homens é: {Homens}')
print(f'O total de mulheres é: {Mulheres}')