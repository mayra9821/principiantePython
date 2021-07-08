"""
HACER UN PROGRAMA QUE MUESTRE TODOS LOS NUMEROS ENTRE DOS NUMEROS QUE DIGA EL USUARIO

"""
numero1 = int(input("primer numero: "))
numero2 = int(input("segundo numero: "))

numero_inmovil = numero1
i = numero1 + 1

for i in range(numero1+1,numero2):
    print(f"los numeros que estan entre {numero_inmovil} y {numero2} son: {i}")
