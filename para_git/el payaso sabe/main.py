import random
from funciones import *

biologia = {
    "pregunta":["¿cuantos cerebros tiene un pulpo?"],
    "res_correcta":["9 cerebros"],
    "res_incorrecta":["2 cerebros","3 cerebros","7 cerebros"]
}

respuestas,verdadera = randomisar_listas_de_respuestas(biologia)
contesto = False

while contesto == False:

    print(f"{biologia["pregunta"]}:")

    for k in range(len(respuestas)):
        print(f"{respuestas[k]}")

    ingreso =(input("ingrese 1,2,3 o 4 para elegir su opcion elegida: "))

    numeros_validos = ["1","2","3","4"]

    mensaje,valido = (verificar_respuesta_correcta(ingreso,respuestas,verdadera))

    if valido == True:
        print(valido)
        contesto = True

    elif valido == False:
        print(valido)
        contesto = False

