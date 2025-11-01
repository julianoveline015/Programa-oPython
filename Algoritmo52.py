import os
os.system('cls' if os.name == 'nt' else 'clear')
import math

base = int(input("Digite a base: "))
altura = int(input("Digite a altura"))

area = (base * altura) * 2
diagonal = math.sqrt(math.pow(base, 2) + math.pow(altura, 2)) * 2
perimetro = 4 * (base + altura)

print(f"Area: {area},\
    \nDiagonal: {diagonal}, \
    \nPerimetro: {perimetro}.")