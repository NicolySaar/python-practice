from fractions import Fraction

desconto = int(input("Insira o desconto: "))
valor = float(input("Insira o valor do produto: "))
fracao = Fraction(desconto, 100)
produto = valor - (valor * fracao)
print(f"O valor do produto é R${valor:.2f} e com desconto de {desconto}%, fica {produto:.2f}.")



