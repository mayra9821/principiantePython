"""
ESCRIBIR UN PROGRAMA QUE MUESTRE LOS CUADRADOS (UN NUMERO MULTIPLICADO POR SI MISMO)
DE LOS 60 PRIMEROS NUMEROS NATURALES. RESOLVERLO CON FOR Y WHILE

"""

contador = 1

for contador in range(1,61):
    resultado = contador * contador
    print(f"el cuadrado de {contador} es: {resultado}")