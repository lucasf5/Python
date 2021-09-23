# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt():
  while True:
    try:
      n = int(input('Digite um numero: '))
    except:
      print('\033[0;31mFormato errado, tente novamente: \033[m')
      continue
    except KeyboardInterrupt:
      print('Usuário não digitou nada!')
      return 0
    else:
      print(f'\033[0;32mO numero digitado foi: {n}\033[m')
      return n


leiaInt()

    