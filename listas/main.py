#este es un string normal
superheroe="superman"
print(type(superheroe))

#manera 1 de declarar lista
superheroes = ["Batman","spiderman","mujer maravilla"]
print(superheroes)


#otra manera de declarar una lista
familia= list((1,2,3))
print(familia)

#lista con atributo range

año = list((range(1998,2021,2)))

print(año)

#se pueden ingresar distintos tipos de variables a una lista

variado = ["otra",4,5.4,True,"texto"]
print(variado)


#como acceder a un elemento de la lista

print(superheroes[1])
print(superheroes[-1])

#si quiero sacar los elementos en cierto rango

print(superheroes[0:2]) #saca los elemento del 0 al 1 hay que sumarle 1 si 
                        #se quiere sacar hasta el elemnto que uno quiera

print(superheroes[0:])

#añadir elemento a una lista con append

superheroes.append("iron man")

print(superheroes)

#recorrer una lista

print("***listado peliculas***")

nueva_pelicula=" "
while nueva_pelicula!="parar":
    nueva_pelicula = input("introduce un nuevo superheroe: ")

    if nueva_pelicula!= "parar":
        superheroes.append(nueva_pelicula)
    
for superheroe in superheroes:
    print(f"{superheroes.index(superheroe)+1}.{superheroe}")

