"""
escribir un programa que guarde en una variable el diccionario {'euro':'€', 'dolar':'$','yen':'¥'}, pregunte al usuario
por una divisa y muestre su simbolo o un mensaje de aviso si la divisa no esta en el diccionario

"""

divisas = {
    'euro':'€', 
    'dolar':'$',
    'yen':'¥'
}

x = input("introduce una divisa: ")

print(divisas.get((x),"esa vaian no esta"))



