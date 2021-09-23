# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt():
  n = input('Digite um numero: ')
  while not n.isnumeric():
    n = input('\033[0;31mFormato errado, tente novamente: \033[m')

  print(f'\033[0;32mO numero digitado foi: {n}\033[m')

leiaInt()
    