import os
os.system('clear')
import math

angulo = int(input("Digite o cosseno: "))

math.radians(angulo)

cos = math.cos(angulo)
sen = math.sin(angulo)
tan = math.tan(angulo)
secante = 1 /sen
cossecante = 1 / cos
cotange = 1 /tan

print(f"Resultados cosseno: \n{cos}, \n{sen}, \n{tan}, \n{secante},\
                            \n{cossecante}, \n{cotange}")