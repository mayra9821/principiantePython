"""
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, 
un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta.
Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

Fruta	Precio
Plátano	1.35
Manzana	0.80
Pera	0.85
Naranja	0.70

"""

frutas ={
    'platano' : 1.35,
    'manzana' : 0.80,
    'pera' : 0.85,
    'naranja' : 0.70
}

fruta=input("que fruta quiere: ")
kilo=0
def calculo(a,b): #se pede hacer sin la función
    if fruta in frutas:
        kilo=float(input("cuantos kilos quiere: "))
        resultado=frutas.get(fruta)*kilo
        print(f"el valor total de  es {resultado}")
    else:
        print("esta fruta no esta")

calculo(fruta,kilo)
