#FUNCION PARA DETERMINAR TIPO DE VARIABLE

nombre = "mayra torres"

tipo = (type(nombre))

print(tipo)

#detectar el tipado

tipo2 = isinstance (nombre,str)

if tipo2 == True:
    print("un string")
else:
    print("no es un  string")


# Limpiar espacios

frase = "                mi contenido             "

print("---------antes--------")
print(frase)
print("---------despues------")
print(frase.strip())


if len(nombre)==0:
    print("esta vaina esta vacia")
else:
    print("esta vaina esta llena",len(nombre))

#encontrar caracteres

frase= "la vida es bella"
print(frase.find("vida"))

#reemplazar palabreas en un string

nueva_frase = frase.replace("vida","moto")
print(nueva_frase)

#mayusculas y minúsculas

print (nombre)
print(nombre.lower())
print(nombre.upper())