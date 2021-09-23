def teste(b):
  global s
  s = 8
  print(f'S dentro vale: {s}')


s = 5
print(f'S fora vale: {s}')
teste(s)



def soma(a,b,c):
  s = a+b+c
  return s

x = soma(2,4,6)
y = soma(2,10,6)
z = soma(14,4,6)

print(f'As somas deram: {x}, {y} e {z}')