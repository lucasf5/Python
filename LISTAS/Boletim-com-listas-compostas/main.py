# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
notas = []
lista = []

while True:
  nome = str(input('Nome: '))
  nota1 = float(input('Nota 1: '))
  nota2 = float(input('Nota 2: '))
  NotaMedia = (nota1+nota2)/2

  lista.append([nome, [nota1, nota2], NotaMedia])

  x = int(input('Sair? [0] Sim [1] Não: \n'))
  if x == 0:
    break

print(f'{"No.":<4}{"NOME:":<10}{"MÉDIA:":>8}')

for i, a in enumerate(lista):
  print(f'{i:<4}{a[0]:<10}{a[2]:>6}')

while True:
  X = int(input('Deseja acessar a nota de qual aluno?\n'))
  print('='*30)
  print(f'{"NOME:"} {lista[X][0]}\n{"NOTAS."} {lista[X][1]}\n{"MÉDIA:"} {lista[X][2]}')
  print('='*30)
  x = int(input('Sair? [0] Sim [1] Não:\n'))
  if x == 0:
    break
