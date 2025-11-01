import os
os.system('cls' if os.name == 'nt' else 'clear')

idade = int(input("Digite sua idade: "))

if(idade >= 0 and idade <= 11):
    print(f"Infantil: {idade}")
elif(idade >= 12 and idade <= 17):
    print(f"Adolescente: {idade}")
elif(idade >= 18 and idade <= 24 ):
    print(f"Jovem: {idade}")
elif(idade >= 90):
    print("Hora extra")
else:
    print(f"Adulto: {idade}")

