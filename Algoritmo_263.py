import os
os.system('cls')

cont=0

while(True):
    numero = int(input("Digite um numero: "))
    if(numero<0):
        break
    cont = cont+1
print(f'A quantidade de numeros digitados foi: {cont}')
