n = float(input('Digite seu numero: '))
x = float(input('Digite seu numero: '))

def moeda():
  return f'R${moeda}{n}'.replace('.', ',')

def aumentar():
  a = n+x
  print(f'Antes tinhamos {n}, com um aumento de {x} agora temos {a}')
def diminuir():
  a = n-x
  print(f'Antes tinhamos {n}, com uma diminuição de {x} agora temos {a}')
def dobro():
  a = n*2
  print(f'Antes tinhamos {n}, com um duplicação, agora temos {a}')
def metade():
  a = n/2
  print(f'Antes tinhamos {n}, com uma divisão, agora temos {a}')


