import os
os.system('cls' if os.name == 'nt' else 'clear')

idade = int(input("Digite sua idade: "))

if(idade <= 16):
    print("Reprovada")
else:
    print("Aceita")



