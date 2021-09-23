import random
# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

palpite = int(input('Digite o numero: '))
x = ''


while x != palpite:
  x = random.randint(0,9)
  print(f'A maquina escolheu: {x}')
  palpite = int(input('Você errou, tente novamente: '))
print(f'Você venceu! Pois o valor da maquina foi {x} e o seu foi {palpite}')