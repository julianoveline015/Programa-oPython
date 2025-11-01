import os
os.system('cls' if os.name == 'nt' else 'clear')

nota01 = float(input("Digite sua nota: "))
nota02 = float(input("Digite sua nota: "))
nota03 = float(input("Digite sua nota: "))
nota04 = float(input("Digite sua nota: "))

media = (nota01 + nota02 + nota03 + nota04) / 4

if(media >= 7):
    print("Aprovada")
else:
    print("Reprovada")
