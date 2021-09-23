# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

total = {}

total['Aluno'] = input('Aluno: ')
total['Media'] = float(input('Media: '))

if total['Media'] >=7:
  total['situação'] = 'Aprovado!'
else:
  total['situação'] = 'Aprovado!'

print(f'O aluno: {total["Aluno"]}')
print(f'Tem a média: {total["Media"]}')
print(f'E está: {total["situação"]}')


