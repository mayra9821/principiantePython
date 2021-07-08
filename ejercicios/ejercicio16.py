"""Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario.
Después debe mostrar or pantalla el mensaje <nombre> tiene <edad> años,
vive en <dirección> y su número de teléfono es <teléfono>.

"""

nombre = input("nombre: ")
edad = input("edad: ")
direccion = input("direccion: ")
telefono = input("telefono: ")

dicc ={
    'nombre':nombre,
    'edad':edad,
    'direccion':direccion,
    'telefono':telefono
}

print(f"{dicc.get('nombre')} tiene {dicc.get('edad')} vive en {dicc.get('direccion')} y su numero de telefono es {dicc.get('telefono')} ")
