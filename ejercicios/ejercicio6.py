"""
hacer un programa que muestre todos los numeros mpares entre dos numeros que decida el usuario

"""

numero1 = int(input("numero 1: "))

numero2 = int(input("numero 2: "))

i = numero1

for i in range(numero1,numero2):
    if i%2==1:
        print(f"numero impar: {i}")