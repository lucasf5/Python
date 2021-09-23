# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


N = int(input('Numero: '))
lista = []
count = 0
S = 0

while S != 1:
  N = int(input('Numero: '))
  lista.append(N)
  count += 1
  S = int(input('Deseja continuar? \n[0]Sim\n[1]Não\n'))

print(f'Foi colocado {count} itens na lista.')
x = (sum(lista)/count)
print(f'A media de todos eles é: {x}')
print(max(lista))
print(min(lista))