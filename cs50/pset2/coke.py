amountdue = 50
print(amountdue)


while amountdue > 0:
    coin = int(input("insert coin: "))
    if coin in [5, 10, 25]:
        amountdue = amountdue - coin
    else:
        amountdue = amountdue - 0
    print(amountdue)

