from datetime import datetime

# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

cadastro = {}

cadastro['nome'] = str(input('Nome: '))
cadastro['anoDeNascimento'] = int(input('Nascimento: '))
cadastro['Trabalho'] = int(input('Trabalhando [0] Não [1] Sim \n'))


if cadastro['Trabalho'] == 1:
  cadastro['anoDeContrato'] = int(input('Ano da contratação: '))
  cadastro['Salario'] = float(input('Digite seu salário: '))
  cadastro['aposentadoria'] = (cadastro["anoDeContrato"] +35)

for k,v in cadastro.items():
  print(f'{k} tem o valor {v}')
