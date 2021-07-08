"""
FUNCIONES:

"""
"""

#ejemplo 1

print("***********ejemplo 1****************")

def muestraNombre():
    print("mayra")
    print("francisco")
    print("jose")
    print("jaira")
    print("juanse")
    print("nury")
    print("\n")

#invocar la funcion o funciones

muestraNombre()
"""
"""
#parametros de una funcion
print("***********ejemplo 2****************")



def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")

    if edad>=18:
        print("eres mayor de edad")
    else:
        print("no eres mayor de edad")

nombre = input ("introduce tu nombre: ")
edad  =int(input("ingresa tu edad"))

mostrarTuNombre(nombre , edad)

"""
"""
#ejemplo 3
print("***********ejemplo 3****************")

def tabla(numero):
    numero = int(input("ingrese numero de tabla de multiplicar"))
    print(f"tabla de multiplicar del numero: {numero}")

    for contador in range(1,11):
        operacion = numero * contador
        print(f"{numero}x{contador} = {operacion}")
    
    print("\n")

tabla("numero")



"""

#ejemplo 4: parametros opcionales

print("------ejemplo 4-----------")

def getEmpleado(nombre,dni =False):
    print("empleado")
    print(f"Nombre: {nombre}")
    print(f"DNI: {dni}")

getEmpleado("mayt","22")


#ejemplo 5: return y ejercicios mas completos

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"

    return saludo

print(saludame("mayra torres"))


#ejemplo 6

print("\n----ejemplo 6--------------")

def calculadora(numero1,numero2,basicas = False ):
    
    suma =numero1+numero2
    resta= numero1-numero2
    multiplicacion = numero1*numero2
    dividion = numero1/numero2

    cadena = ""
    if basicas != False:
        cadena += "suma: "+str(suma)
        cadena += "\n"
        cadena += "resta: "+str(resta)
        cadena += "\n"
    else:
        cadena += "multiplicacion: "+str(multiplicacion)
        cadena += "\n"
        cadena += "division: "+str(dividion)


    return cadena

print(calculadora(56,5))



