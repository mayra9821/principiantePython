import os, shutil
import pathlib

#crear carpeta

# if not os.path.isdir("c:/Users/MayTo/Documents/PYTHON/curso_python/level1/sistema-archivos/miCarpeta"):
#     os.mkdir("c:/Users/MayTo/Documents/PYTHON/curso_python/level1/sistema-archivos/miCarpeta")
# else: print("ya existe")

#eliminar carpeta
# os.rmdir("c:/Users/MayTo/Documents/PYTHON/curso_python/level1/sistema-archivos/miCarpeta")

#copiar carpeta
# rutaOriginal = str(pathlib.Path().absolute())+"\sistema-archivos/miCarpeta"
# rutaNueva = str(pathlib.Path().absolute())+"\sistema-archivos/miCarpeta_copiada"

# shutil.copytree(rutaOriginal,rutaNueva)

##listar archivos de carpetas

print("Contenido de mi carpeta:")
contenido = os.listdir("c:/Users/MayTo/Documents/PYTHON/curso_python/level1/sistema-archivos/miCarpeta_copiada")
print(contenido)

for archivo in contenido:
    print(f"fichero: {archivo} ")

