"""
crear un script que tenga 4 variables, una lista, un string, un entero y un booleano y que imprima un mensaje 
segun el tipo de dato de cada variable. usar funciones


"""
lista = ["mayra",89,"la visa"]
string = "esto es un string"
num = int(98)
booleano=True

def tipo_var (dato,tipo):
    comprobar =isinstance(dato,tipo)
    msj = " "
    if comprobar:
        msj =f"este dato {dato} es de tipo {tipo}"
    else:
        msj = "el sato no es de este tipo"
    
    return msj

print(tipo_var(lista,str))