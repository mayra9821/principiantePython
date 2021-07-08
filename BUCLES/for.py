""" 
FOR

for variable in elemento_iterable (lista,rango,etc)
    bloque de instrucciones

"""

#ejemplo 1
"""
contador = 0
resultado = 0
for contador in range(0,10):
    print("\n: ",contador)
    resultado += contador 

print(f"la suma de todo es: {resultado}")

"""
#ejemplo con tablas de multiplicar

print("***************EJEMPLO TABLAS DE MULTIPLICAR************************")

numero_usuario = int(input("de que numero quieres la tabla de multiplicar: "))

if numero_usuario < 1:
    print("ey amigo!! pusiste un numero menor a uno,solo numeros positivos para la tabla de multiplicar")
    numero_usuario = 1
elif numero_usuario >= 1:
    print("los numeros de la tabla de multiplicar del numero escogido son:")
    i=0
    for i in range (1,11):
        resultado = numero_usuario*i
        print(f"{numero_usuario}x{i}={resultado}")
        
print("tabla terminada")



