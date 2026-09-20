from fractions import Fraction
salário = float(input('Qual é o salário do funcionário?: '))
aumento =  int(input("Insira o aumento: "))
fracao = Fraction(aumento, 100)
novosalário = salário + (salário * fracao)

print(f"O funcionário que ganhava {salário:.2f}, e com aumento de {aumento}% vai passar a ganhar {novosalário:.2f} após o aumento.")
