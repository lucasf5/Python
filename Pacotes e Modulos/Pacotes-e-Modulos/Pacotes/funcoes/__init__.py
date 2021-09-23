def soma(a,b):
  x = a+b
  print(f'A soma de {a} + {b} = {x}')

def fatorial(n):
  count = n
  while count != 1:
    print(f'{count}', end=' x ')
    count-=1
    if count == 1:
      print(f'{count}', end=' = ')
  f = 1
  for i in range(1, n+1):
    f *= i
  print(f)