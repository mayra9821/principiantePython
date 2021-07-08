print("\n**************LISTADO DE CONTACTOS**************")

contactos = [
    [
        'atonio',
        'antoni@gmail.com'
    ],
    [
        'jose',
        'jose@gmail.com'
    ],
    [
        '0pancito',
        'pancito@gmail.cm'
    ]
]

print(contactos[0][1])

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("nombre: "+elemento)
        else:
            print("correo: "+elemento)
    print("\n")


