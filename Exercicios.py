import os
os.system('cls' if os.name == 'nt' else 'clear')

altura = float(input("Digite sua altura: "))
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))

if(altura < 1.70 and idade <= 16):
    print(f"Sua idade e altura foram aprovados !")
elif(peso < 60):
    print(f"Aprovada")
else:
    print("Reprovada")
