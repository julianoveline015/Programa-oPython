import os
os.system('cls' if os.name == 'nt' else 'clear')

numero = int(input("Digite um número: "))

if(numero >= 20 and numero <= 90):
    print(f"O número {numero} está entre 20 e 90.")
else:
    print("Não está entre os número.")