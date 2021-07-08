"""
Modulos: funcionalidades ya hechas para reutilizar.

Para obtener informacion:
https://docs.python.org/3/py-modindex.html

podemos conseguir modulos que vienen en el lenguaje, modulos en internet y tambien podemos crear
nuestros modulos.

"""

################CREAR MODULOS########

import mimodulo
##otra manera
## from mimodulo import*
## from mimodulo import (funcion definida dentro del modulo)
## from mimodulo import HolaMundo
print(mimodulo.HolaMundo("mayra torres"))

x=mimodulo.calculadora(3,2)

print(x)