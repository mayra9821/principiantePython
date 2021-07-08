"""
    DICCIONARIO: un tipo de dato que almacena un conjunto de datos.
    en formato clave con un valor
    es parecido a un array asociativo o un objeto json

"""

diccionario = {

    "mayra":"hermosa",
    "jairtih":"fea",
    "jose":"novio"
}

print(type(diccionario))

#lista con diccionarios

contactos = [
    {
        "nombre":'valor',
        'email':'tumami@gmial,,ovm'
    },
    {
        'nombre':'luis',
        'email': 'luis.com'
    }
]

#para modificar un elemento dentro del diccionario que esta contenido en la lista
contactos[0]['nombre']="mayra"
print(contactos)


for contacto in contactos:
    print(f"nombre: {contacto['nombre']}")
    print(f"correo electronico: {contacto['email']}")
    print("-----------------------------------------------")

