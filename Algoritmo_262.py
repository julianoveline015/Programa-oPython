import os
os.system('cls')

while(True):
    numero = int(input("Digite um numero: "))
    if(numero == -999):
        break
    else:
        numero = numero*3
        print(f"Triplo: {numero}")