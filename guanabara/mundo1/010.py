saldo = float(input('Digite quanto dinheiro você tem na carteira:? R$'))

dol = saldo / 5.14
euro = saldo / 6.00

print('Com esse valor, você pode comprar: \n{:.2f} dólares \n{:.2f} euros'.format(dol, euro))