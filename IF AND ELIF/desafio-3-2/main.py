# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

# – O primeiro valor é maior

# – O segundo valor é maior

# – Não existe valor maior, os dois são iguais.


x = int(input('Digite um numero:'))
y = int(input('Digite um numero:'))


if x > y:
  print('O primeiro valor é maior!')
  print('O segundo valor é menor!')
elif x < y:
  print('O segundo valor é maior!')
  print('O primeiro valor é menor!')
elif x == y:
  print('Não existe valor maior, os dois são iguais.')