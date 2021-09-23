# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
x =input('Digite seu sexo [M/F]: ').upper()

while x!='M' and x!='F':
  x = input('Errado! Tente novamente: ').upper()
print(f'Aceito! \nSexo: {x}')


