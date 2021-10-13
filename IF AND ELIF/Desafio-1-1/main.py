# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

Casa = int(input("Valor da casa: "))
Salario = int(input("Valor do salario: "))
Anos = int(input("Anos de pagamento da casa: "))

Anos *= 12
ValorMensal = Casa / Anos
NovoSalario = Salario * 0.30

if ValorMensal > NovoSalario:
    print("Emprestimo negado!")
elif ValorMensal < NovoSalario:
    print("Emprestimo Condecido!")

print(f"30% do seu salário é {NovoSalario} e o valor da prestação é {ValorMensal}")