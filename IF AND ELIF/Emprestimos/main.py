from time import sleep
# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto

# – à vista no cartão: 5% de desconto

# – em até 2x no cartão: preço formal 

# – 3x ou mais no cartão: 20% de juros

produto = float(input('Digite o valor do produto: '))
pagamento = int(input('Forma de pagamento\n\n[0]Dinheiro\n[1]Cheque\n[2]Cartão\nDigite: '))
parcelamento = int(input('Quantas vezes: \n[0]1x \n[1]2x \n[2]3x ou mais.\nDigite:'))

print('\033[7;33mProcessando seu pagamento...\033[m')
sleep(2)
print('\033[7;32mPagamento processado!\033[m')
sleep(1)
print(f'\033[7;30;44mInformações digitadas: \nO valor total do produto é: {produto}\nO modo de pagamento é: {pagamento}\nO numero de parcelas: {parcelamento}\033[m')

if parcelamento == 0 and (pagamento == 0 or pagamento == 1):
  produto = produto - (produto*0.10)
  print(f'O valor do produto atual é: {produto}')
elif parcelamento == 0 and (pagamento == 2):
  produto = produto - (produto*0.05)
  print(f'O valor do produto atual é: {produto}')
elif parcelamento == 1 and (pagamento == 2):
  print(f'O valor do produto atual é: {produto}')
elif parcelamento == 2 and (pagamento == 2):
  produto = produto + (produto*0.20)
  print(f'O valor do produto atual é: {produto}')

