from datetime import date
# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
atual = date.today()
print(atual)
anoatual = atual.year

count = 0

for i in range(1,8):
  data = int(input('Ano de nascimento: '))
  maioridade = anoatual-data 
  if maioridade >= 18:
    count += 1

print(f'{count} pessoas estão na maioridade')

