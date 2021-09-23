# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 

# A) Quantas pessoas foram cadastradas 
# B) A média de idade 
# C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média.

registro = {}
Geral = []
Idade = []
while True:
  registro.clear()
  registro["nome"] = str(input('Nome: '))
  registro["sexo"] = str(input('Sexo M/F: ')).upper()
  registro["idade"] = int(input('Idade: '))
  Idade.append(registro["idade"])  

  Geral.append(registro.copy())

  x = str(input('Deseja Continuar S/N: ')).upper()
  if x == 'N':
    break

media = (sum(Idade))/len(Idade)
print(Geral)
print(f'A quantidade de pessoas cadastradas são: {len(Geral)}')
print(f'A media das idades é: {media}')
print(f'Quantidade de pessoas do sexo F: ', end = '')
for p in Geral:
  if p['sexo'] == 'F':
    print(f'{p["nome"]}', end='')

print(f'\nPessoas a cima da média: ')
for p in Geral:
  if p['idade'] >= media:
    print(f'{p}', end='')
