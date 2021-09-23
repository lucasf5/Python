# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

mediaidade = ''
nomelista = []
idadelista = []
sexolista = []

homens = []
mulherescommenosde20 = 0
nomedelas = []


# -------------------------------------------------------------------
for i in range(1,5):
  print(f'{i} PESSOA')
  nome = (input('Seu nome: '))
  idade = int(input('Sua idade: '))
  sexo = int(input('Sexo? [0]Masculino [1]Feminino: '))
  if sexo == 1 and idade < 20:
    nomedelas.append(nome)
    mulherescommenosde20 += 1
  elif sexo == 0:
    homens.append(nome)
  

# Adcionei todas idades em uma lista
  idadelista.append(idade)
# Tirei a média dessas idades //Primeira parte
  mediaidade = ((sum(idadelista))/4)

# Adcionei todos os nomes em uma lista
  nomelista.append(nome)


# -------------------------------------------------------------------
# Armazenei em maximo o maior valor encontrado dentro de uma lista
maximo = max(idadelista)
# Armazenei em idadexidade o INDEX do maior valor
indexidade = idadelista.index(maximo)

# Armazenei em indexnome a posição de quem tem a maior idade
indexnome = nomelista[indexidade]


# -------------------------------------------------------------------
print(f'A media das idades é: {mediaidade}')
print(f'A pessoa que tem a maior idade, com {maximo} é essa: {indexnome}')
print(f'As mulheres que possuem menos de 20 anos: {mulherescommenosde20} e são: {nomedelas}')






  
