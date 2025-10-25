import os
os.system('clear')

"""Fazer um algoritmo que possa entrar com o saldo de uma aplicação e imprima
o novo saldo, considerando o reajuste de 1%."""
saldo = float(input("Digite seu saldo: "))
novoSaldo = saldo * 0.1
print(f"Saldo: {saldo} \nReajuste: {novoSaldo}")