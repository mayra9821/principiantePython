"""
¿cuanto es el x por ciento de x numero?

            20% de 150
"""

numero = int(input("ingrese el numero: "))

numero_porcentaje = int(input("de cuanto quiere el porcentaje: "))

porcentaje = numero_porcentaje/100

if numero_porcentaje<100:
    resultado = numero * porcentaje
    print(f"el {numero_porcentaje}% de {numero} es : {resultado}")
