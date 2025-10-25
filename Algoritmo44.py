import os
os.system('clear')
import math

"""Entrar com o número e a base em que se deseja calcular o logaritmo desse
número e imprimi-lo."""
numero = int(input("Digite um número: "))
base = int(input("Digite a base: "))

logaritmo = math.log(numero, base)
print(f"Número e base: {logaritmo}")
