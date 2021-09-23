# Try:
#   Operação
# Except:
#   Falhou
# Else:
#   Deu Certo
# Finally:
#   Certo/Falhou




try:
  print(x)
except:
  print('Erro no valor!')
  print('Você não declarou a várivel.')

try:
  x = int(input('Numerador:'))
  y = int(input('Denominador:'))
  a = x/y
  print(f'{a:.2f}')
except ZeroDivisionError:
  print('Não pode divisão por zero!')
else:
  print(a)
finally:
  print('No erro ou acerto, sou imprimido...')

try:
  print(z)

except (ValueError, TypeError, NameError):
  print('Erro no valor!')
  print('Você não declarou a várivel.')