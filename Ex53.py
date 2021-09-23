# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

x = str(input('Digite a sua frase: ')).strip().upper()

# separei cada frase em uma lista
x = x.split()
# juntei tudo em uma string só
junto = ''.join(x)

count = len(junto)

# INVERSO => UTILIZADO NO FOR
inverso = ''


# INVERSO => USANDO OUTRA FORMA
inverso = junto[::-1]


# Como começa em 0. São o numero de letras - 1, pois se fosse 8, seria 7.
# Vai de 7, até -1, que é o ultimo, de 1 em 1, pelo oposto.

# -------forma usando for-----------
# for i in range(count -1, -1, -1):
#   inverso += junto[i]
# ----------------------------------

print(junto, inverso)
if junto == inverso:
  print('É um palíndromo!')
else:
  print('Não é um palíndromo!')


