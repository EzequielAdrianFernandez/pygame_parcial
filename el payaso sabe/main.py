import random
from funciones import *
from base_de_datos import *

respuestas,verdadera = randomisar_listas_de_respuestas(biologia)
#print(respuestas,verdadera) EL ERROR NO ESTA ACA
contesto = False

while contesto == False:

    print(f"{biologia["pregunta"]}:")

    for k in range(len(respuestas)):
        print(f"{respuestas[k]}")

    ingreso =input("ingrese 1,2,3 o 4 para elegir su opcion elegida: ")
    numeros_validos = ["1","2","3","4"]
    mensaje,valido = (verificar_respuesta_correcta(ingreso,respuestas,verdadera))

    if valido == True:
        print(mensaje)
        contesto = True

    elif valido == False:
        print(mensaje)
        contesto = False

    #xd
