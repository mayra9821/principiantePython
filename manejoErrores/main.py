#capturar excepciones y manejar errores en codigo
#suceptibles a fallos/errores

# try:
#     nombre= input("igresa tu nombre: ")

#     if len(nombre)>1:
#         nombre_usuario = "El nombre es"+nombre
        
#     print(nombre_usuario)
# except:
#     print("ha ocurrido un error, mete el nombre puto")
# else:
#     print("todo bien")
# finally:
#     print("fin de la iteracion!!")


##Multiples Excepciones

#try:
#    numero = int(input("ingrese un numero: "))
#    print("El cuadrado del numero es: "+str(numero*numero))
# except TypeError:
#     print("debes convertir tus cadenas a enteros")
# except ValueError:
#     print("tu entrada debe ser un numero")
# except Exception as e:
#     print(type(e))
#     print("ha ocurrido un error: ",type(e).__name__)


#Excepciones Peronalizadas o lanzar excepcion


try:
    nombre = input("ingresa el nombre: ")
    edad = int(input("ingresa la edad: "))
    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no está completo")
    else:
        print(f"Bienvenido al master en Python {nombre}")
except ValueError:
    print("introdce los datos correctamente !!")
except Exception as e:
    print("Existe un error",e);