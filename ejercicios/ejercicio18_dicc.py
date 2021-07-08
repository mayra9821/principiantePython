"""
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla 
la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

"""
meses ={
    1:'enero',
    2:'febrero',
    3:'marzo',
    4:'abril',
    5:'mayo',
    6:'junio',
    7:'julio',
    8:'agosto',
    9:'septiembre',
    10:'octubre',
    11:'noviembre',
    12:'diciembre'
}

x = input("ingrese la fecha en formato dd/mm/aaaa: ")
l=x.split('/')
print(f"la fecha es {l[0]} de {meses.get(int(l[1]))} del {l[2]}  ")

