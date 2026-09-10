def lin():
    print('='*30)


lin()
print("     CÁLCULADORA DE IMC      ")
lin()

nome: str = str(input("Nome: ")).title()
peso: float = float(input("Peso (kg): "))
altura: float = float(input("Altura (m): "))

imc: float = peso / (altura ** 2)

print(f"\nResultado para {nome}:")
print(f"  Peso: {peso:.2f} kg")
print(f"  Altura: {altura:.2f} m")
print(f"  IMC: {imc:.2f}")

if imc <18.5:
    classif = "Abaixo do Peso."
elif imc <25.00:
    classif = "Peso Normal."
elif imc <30.00:
    classif = "Sobrepeso."
else:
    classif = "Obesidade."

print(f"Classificação: {classif}")
lin()