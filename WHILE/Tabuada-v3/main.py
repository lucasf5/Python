
# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

# Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

N = int(input('O valor que quer é: '))

while N > 0:
  for i in range(0,10):
    print(f'{N}*{i} = {N*i}')
  N = int(input('O valor que quer é: ')) 
print('Valor negativo! Interrompido.') 