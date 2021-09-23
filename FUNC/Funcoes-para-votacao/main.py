# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto():
  idade = int(input('Qual sua idade?'))
  if idade >=16 and idade <18:
    print(f'Sua idade de {idade} torna seu voto OPCIONAL')
  elif idade < 16:
    print(f'Sua idade de {idade} torna seu voto NEGADO')
  elif idade >18:
    print(f'Sua idade de {idade} torna seu voto OBRIGATÓRIO')


voto()