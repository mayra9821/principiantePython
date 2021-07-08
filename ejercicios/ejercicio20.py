"""
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una 
persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario.
Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

"""

persona={

}
print("ingrese item y contenido\n\"PARAR\"para salir del ciclo")
item_persona=0
while True:
    item_persona=input("ingrese eiteml : ")
    contenido_item=input("ingrese el contenido: ")
    persona[item_persona]=contenido_item
    if item_persona=="parar":
        persona.pop("parar")
        break

print(persona)
