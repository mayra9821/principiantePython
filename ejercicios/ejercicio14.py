"""
crear una lista con el contenido de esta tabla:
ACCION          AVENTURA                DEPORTES
GTA             ASSINS                  FIFA21  
COD             CRASH                    PRO21
PUBG            PRINCE OF PERSIA        MOTO GP 21

mostrar esta informacion ordenada

"""
tabla = [
    {
        "categoria":"accion",
        "juegos":["gta","cod","pubg"]
    },
    {
        "categoria":"aventura",
        "juegos":["assins", "crash","prince of persia"]
    },
    {
        "categoria":"deportes",
        "juegos":["fifa21", "pro21","moto gp 21"]
    }
]


for categorias in tabla:
    print(f"-----{categorias['categoria']}-----")
    for juego in categorias['juegos']:
        print(juego)

