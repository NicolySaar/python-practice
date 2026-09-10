text = str(input("Digite algo: "))

words = text.split()

camelcase = words[0].lower()

for word in words[1:]:
    camelcase += word.capitalize()

snake_case = "_".join(words).lower()


print(f"camelCase : {camelcase}")
print(f"snake_case : {snake_case}")




