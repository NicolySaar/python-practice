text = input("Input: ")

vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")

result = ""

for letter in text:
    if letter in vowels:
        pass
    else:
        result += letter

print(result)

