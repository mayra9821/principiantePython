"""
el programa tiene que pedir la nota de 15 alumnos y sacar por pantalla cuantos han aprobado y cuantos 
han suspendido

"""

contador = 1
aprobados = 0
suspendidos = 0

numero_alumnos = int(input("cuantos alumnos tienes?: "))

while contador <= numero_alumnos:
    nota = int(input(f"que nota le quieres poner al \"alumno{contador}\""))

    if nota <= 5:
        suspendidos += 1
    elif nota >= 6 or nota <=10 :
        aprobados += 1
    
    contador += 1

print(f"los aprobados son: {aprobados}\n\ry los suspendidos son: {suspendidos}")


