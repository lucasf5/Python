# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

# A) qual é o total gasto na compra.

# B) quantos produtos custam mais de R$1000.

# C) qual é o nome do produto mais barato.

preçototal = []
totalnomes = []
total = 0

while True:
  print('----CADASTRO DE PRODUTO----')
  nome = str(input('Digite o nome do produto: '))
  totalnomes.append(nome)
  preço = float(input('Digite o valor do produto: '))
  preçototal.append(preço)
  if preço > 1000:
    total +=1

  saida = ' '
  while saida not in 'SN':
    saida = str(input('Deseja sair: [s/n]')).strip().upper()
  if saida == 'S':
      break
print('Fim!')
  
menor = min(preçototal)
x = preçototal.index(menor)

print(f'O produto com menor valor é: {totalnomes[x]} com o valor de {menor}')

print(f'Temos {total} produtos com valor maior que 1000.')

print(f'Total gasto é {sum(preçototal)}')
