import os

#puntajes en base 100 puntos
#declarar variables
alumno,puntaje1,puntaje2,puntaje3,puntaje4,puntaje5="",0.0,0.0,0.0,0.0,0.0
puntaje_final=0.0

#INPUT
alumno=os.sys.argv[1]
puntaje1=int(os.sys.argv[2])
puntaje2=int(os.sys.argv[3])
puntaje3=int(os.sys.argv[4])
puntaje4=int(os.sys.argv[5])
puntaje5=int(os.sys.argv[6])

#PROCESSING
puntaje_final=int((puntaje1+puntaje2+puntaje3+puntaje4+puntaje5)/5)

#OUPUT
print(" NOTAS DE EXAMENES")
print(" El alumno: ", alumno)
print("obtubo los siguientes puntajes")
print("primer puntaje: ", puntaje1)
print("segundo puntaje: ", puntaje2)
print("tercer puntaje: ", puntaje3)
print("cuarto puntaje: ", puntaje4)
print("quinto puntaje: ", puntaje5)
print("puntaje final: ", puntaje_final)
print("COMENTARIO:")

#condicional multiple
#SI el puntaje final es mayor a 85 mostrar al estudiante que gano una beca
#SI el puntaje final es menor a 85 pero mayor a 65 mostrar que ha ganado media beca
#SI el puntaje final es menor a 65 mostrar que no alcanzo vacante

if(puntaje_final>=85):
    print("MARAVILLOSO LOGRO")
    print("GANASTE UNA BECA")
if(puntaje_final>=65 and puntaje_final<85):
    print("FELICIDADES")
    print("GANASTE MEDIA BECA")
if(puntaje_final<65):
    print("lo sentimos, no pudo alcanzar vacante ")
#fin_if
