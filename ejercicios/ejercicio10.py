"""
hacer un programa que tenga una lita de 8 numeros enteros
- recorrer la lista y mostrarla, 
-hacerla en una funcion que recorra listas de numeros y devuelva un string para mostar
- ordenarla y mostrarla
- mostrar su longitud
- buscar algun elemento (que el usuario pida por teclado)

"""
numeros = [4,65,76,23,1,2,45,98]

def recorrer(numeros):
    numeros.sort()
    for numero in numeros:
        print(numero)
    print(f"el largo de la lista es {len(numeros)}")


recorrer(numeros)


#para buscar un elemento de la lista

busq=int(input("que numero de la lista quieres: "))

verif = isinstance(busq,int)

buscador = (numeros.index(busq)) +1
print(f"el numero {busq} tiene el lugar #{buscador} en la lista")






