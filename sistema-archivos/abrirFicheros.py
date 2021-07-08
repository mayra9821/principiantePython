import io
import pathlib
import shutil
import os
###abrir archivo

##COPIAR LA RUTA COMPLETA PARA PODER CREAR EL ARCHIVO TXT DENTRO DE LA CARPETA DESEADA
# archivo = open("c:/Users/MayTo/Documents/PYTHON/curso_python/level1/sistema-archivos/fichero_texto.txt","a+")
#ruta = str(pathlib.Path().absolute())+ "/fichero_texto.txt"
#print(ruta)
#print(pathlib.PurePath(ruta).suffix)  ### para mostrar la extensión del archivo 
#print(pathlib.Path.cwd()) ##muestra el directorio actual
#print(pathlib.Path.home()) ##devuelve la ruta de inicio del usuario
ruta = open(str(pathlib.Path().absolute())+"\sistema-archivos/ficherto.txt","a+")
ruta.write("hola choi mayra\n")
#archivo_lectura = open("c:/Users/MayTo/Documents/PYTHON/curso_python/level1/sistema-archivos/fichero_texto.txt","r")
#escribir dentro del archivo
#archivo.write ("**soy una figura***\n")

##cerrar archivo
ruta.close()

#### Leer contenido
# lista = archivo_lectura.readlines()
# archivo_lectura.close()

# for elemento in lista:
#     lista_elemento= elemento.split()
#     print(lista_elemento)

#copiar un archivo

# rutaOriginal = str(pathlib.Path().absolute())+"\sistema-archivos/ficherto.txt"
# rutaCopiada = str(pathlib.Path().absolute())+"\sistema-archivos/fichertoCopiado.txt"
# rutaAleternativa = str(pathlib.Path().absolute())+"\modulos/fichertoCopiado.txt"
# shutil.copyfile(rutaOriginal,rutaAleternativa)

#Renomabrar un archivo
# rutaOriginal = str(pathlib.Path().absolute())+"\sistema-archivos/fichertoCopiado.txt"
# rutaNueva = str(pathlib.Path().absolute())+"\sistema-archivos/fichero_CopiadoNUEVO.txt"

# shutil.move(rutaOriginal,rutaNueva)

#eliminar archivos
# rutaNueva=str(pathlib.Path().absolute())+"\sistema-archivos/fichero_CopiadoNUEVO.txt"
# os.remove(rutaNueva)

import os.path
#Comprobar si el archivo existe
rutaNueva = os.path.abspath("./")+"\sistema-archivos/ficherto.txt"

print(rutaNueva)

if os.path.isfile(rutaNueva):
    print("El archivo existe")
else: print ("El archivo no existe")