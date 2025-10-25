import os
os.system('cls')

cont = 0
acm = 0

while(True):
    numero = int(input("Digite um numero: "))
    if(numero == 0):
        break
    acm = acm+numero
    cont = cont+1

media = acm/cont
print(f'total: {acm}, média: {media}')