"""
funciones dentro de otras funciones

"""

def getNombre (nombre):
    texto = f"el nombre es {nombre}"

    return texto

def getApellidos(apellidos):
    texto = f"el apellido es {apellidos}"

    return texto

def devulveTodo(nombre,apellidos):
    texto = getNombre("mayra")+"\n"+getApellidos("torres")

    return texto

print(devulveTodo("nombre","apellidos"))