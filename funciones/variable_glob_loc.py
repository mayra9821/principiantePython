"""
VARIABLES LOCALES: se definen dentro de la función y no se puede usar fuera de ella, solo están disponibles dentro.
a no ser que hagamos un return.

VAIRABLES GLOBALES: Son las que se declaran fuera de una funcion y estan disponibles dentro y fuera de ellas.

"""

#variable global

frase = "ni los genios son tan genios, ni los mediocres tan mediocres"

print(frase)

def HolaMundo():
    frase="hola mundo!!"
    print("dentro de la funcion:")
    print(frase)

    year = 2021
    print(year)

    global website
    website = "mayratorres@gmail.com"
    print("DENTRO: ",website)


    return "Dato devuelto" + str(year)

print(HolaMundo())
print("FUERA: ",website)
