cantantes = ["Beyoncé","Sia","Sahwn Mendez","Camila cabello","Beyoncé"]
numeros=list((1,3,5,7,3,2,6,8,89,5,3,2,45))
#buscar denntro de la lista

print('Sahwn Mendez' in cantantes)

#contar los elementos de la lista

print(cantantes)
print(len(cantantes))


#saber cuantas veces aparece un elemento
print(cantantes.count("Beyoncé"))


#saber el indice
print(cantantes.index("Sahwn Mendez"))

#unir una lista con otra
cantantes.extend(numeros)

print(cantantes)

#eliminar elementos de una lista
cantantes.pop(2)
cantantes.remove('Sia')
print(cantantes)