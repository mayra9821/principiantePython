#formas para concatenar strings


nombre = "mayra"
apellidos = "torres sumalave"
correo = "mayraalejandratorressumalave@gmail.com"


#forma 1 = con signo +
#print( 'hola mi nombre es '+ nombre +" "+ apellidos +' \ny mi correo es'+correo)

#forma 2 = con la letra f
#print("hola mi nombre es {}".format(nombre))

#forma 3= con .format
print("hola soy {} {}{}".format(nombre,apellidos,correo))
