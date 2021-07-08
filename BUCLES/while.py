####CICLO WHILE####
"""
contador = 1
muestrame = str(0)

while contador <= 100:
    print(f"voy por el numero: {contador}")
    contador += 1

while contador <= 100:
    muestrame = muestrame +","+ str(contador)
    contador += 1
print(f"voy por el numero: {muestrame}")
"""
print("*****TABLAS DE MULTIPLICAR*****")

valor_tabla = int(input("De que numero quieres la tabla?: "))
contador = 1
resultado = int(0)

while contador <= 10:
    resultado = valor_tabla * contador 
    print(f"{valor_tabla}x{contador}={resultado}")
    contador += 1

iteracion=(input("quieres saber otra tabla de multiplicar? "))

while iteracion == "si":
    valor_tabla2=int(input("de que valor quieres la tabla?: "))
    contador = 1
    resultado = 0
    while contador <= 10:
        resultado = valor_tabla2 * contador 
        contador += 1
        print(f"{valor_tabla2}x{contador}={resultado}")

if iteracion == "no":
    exit