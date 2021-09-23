# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

# [ 1 ] somar

# [ 2 ] multiplicar

# [ 3 ] maior

# [ 4 ] novos números

# [ 5 ] sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso.
print('='*40)
print('          ----- VALORES -----')
print('='*40)

x = int(input('Digite um numero: '))
y = int(input('Digite um numero: '))
print('='*40)
valor = int(input('Digite sua opção \n[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa\nEscolha: '))

while valor != 5:
  if valor == 1:
    print('-'*40)
    print('Você escolheu a soma!')
    print('='*40)
    print(f'O numero {x} + {y} = {x+y}')
    print('='*40)
    valor = int(input('Digite sua opção \n[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa\nEscolha: \n'))
    
  if valor == 2:
    print('Você escolheu a multiplicação!')
    print('='*40)
    print(f'O numero {x} * {y} = {x*y}')
    print('='*40)
    valor = int(input('Digite sua opção \n[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa\nEscolha: \n'))
  if valor == 3:
    if x > y:
      print('='*40)
      print(f'O maior valor é {x}')
      print('='*40)
    elif x < y:
      print('='*40)
      print(f'O maior valor é {y}')
      print('='*40)
    elif x == y:
      print('='*40)
      print(f'Os valores são iguais!')
      print('='*40)
    valor = int(input('Digite sua opção \n[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa\nEscolha: \n'))
  if valor == 4:
    print('='*40)
    x = int(input('Digite um numero: '))
    y = int(input('Digite um numero: '))
    valor = int(input('Digite sua opção \n[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa\nEscolha: \n'))
  
else: print('Você escolheu sair do programa!')
