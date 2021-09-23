import random

x = random.choices(('pedra', 'papel', 'tesoura'),k=1)
x = (", ".join(x))

escolha = int(input('\n[0] PEDRA\n[1] PAPEL\n[2] TESOURA \nESCOLHA: '))

if x == 'pedra' and escolha == 0:
  escolha = 'PEDRA'
  print(f'A maquina escolheu: {x}')
  print(f'Você escolheu: {escolha}')
  print('Empate!')
elif x == 'pedra' and escolha == 1:
  escolha = 'PAPEL'
  print(f'A maquina escolheu: {x}')
  print(f'Você escolheu: {escolha}')
  print('Venceu!')
elif x == 'pedra' and escolha == 2:
  escolha = 'TESOURA'
  print(f'A maquina escolheu: {x}')
  print(f'Você escolheu: {escolha}')
  print('Perdeu!')

elif x == 'papel' and escolha == 1:
  escolha = 'PAPEL'
  print(f'A maquina escolheu: {x}')
  print(f'Você escolheu: {escolha}')
  print('Empate!')
elif x == 'papel' and escolha == 2:
  escolha = 'TESOURA'
  print(f'A maquina escolheu: {x}')
  print(f'Você escolheu: {escolha}')
  print('Venceu!')
elif x == 'papel' and escolha == 0:
  escolha = 'PEDRA'
  print(f'A maquina escolheu: {x}')
  print(f'Você escolheu: {escolha}')
  print('Perdeu!')

elif x == 'tesoura' and escolha == 2:
  escolha = 'TESOURA'
  print(f'A maquina escolheu: {x}')
  print(f'Você escolheu: {escolha}')
  print('Empate!')
elif x == 'tesoura' and escolha == 0:
  escolha = 'PEDRA'
  print(f'A maquina escolheu: {x}')
  print(f'Você escolheu: {escolha}')
  print('Venceu!')
elif x == 'tesoura' and escolha == 1:
  escolha = 'PAPEL'
  print(f'A maquina escolheu: {x}')
  print(f'Você escolheu: {escolha}')
  print('Perdeu!')

