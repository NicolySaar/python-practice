nome = str(input("Digite o seu nome: ")).strip()

print("Analisando seu nome...")
print("Seu nome em letras maiúsculas é {}".format(nome.upper()))
print("Seu nome em letra minúsculas é {}".format(nome.lower()))
print("Seu nome tem {} letras".format(len(nome) - nome.count(' ')))

nomesep = nome.split()
print("Seu primeiro nome é {} e tem {} letras".format(nomesep[0], len(nomesep[0])))