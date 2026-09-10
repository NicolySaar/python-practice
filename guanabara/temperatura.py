def lin():
    print('='*30)

lin()
print("     CONVERSOR DE TEMPERATURA     ")
lin()
print("1 - Converter Celsius")
print("2 - Converter Fahrenheit")
print("3 - Converter Kelvin")

menu = int(input("Escolha uma opção: "))

if menu == 1:
    C = float(input("Informe a temperatura em °C: "))
    F = C * 1.8 + 32
    K = C + 273.15
    print(f"A temperatura de {C}°C corresponde a")
    print(f"{F:.2f}°F e {K:.2f}°K")

elif menu == 2:
    F = float(input("Informe a temperatura em °F: "))
    C = (F - 32) / 1.8
    K = (F - 32) / 1.8 + 273.15
    print(f"A temperatura de {F}°F corresponde a")
    print(f"{C:.2f}°C e {K:.2f}°K")

elif menu == 3:
    K = input("Informe a temperatura em °K:")
    C = K - 273.15
    F = (K - 273.15) * 1.8 + 32
    print(f"A temperatura {K}°K corresponde a")
    print(f"{C:.2f}°C e {F:.2f}°F")

else:
    print("Opção Inválida!")