senha = input('Digite a senha: ')

while senha != 'letscode':
  print('senha invalida!')
  senha = input('Tente de novo: ')
else: print('Senha valida!')

x = 0
while x <= 20:
  print(f'valor de {x} é menor que 20')
  x += 2
print('Fim!')