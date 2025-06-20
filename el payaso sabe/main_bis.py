import puntaje_tickets
import usuarios
import random
from funciones_bis import *
from base_de_datos_bis import *

correctas = 0
incorrectas = 0
contesto = False

dificultades=["facil","medio","dificil"]
num_tem = random.randint(0,2)
dificultad = dificultades[num_tem]
categoria , pregunta = seleccionar_pregunta(biblioteca_preguntas,dificultad)
respuestas , verdadera = randomisar_listas_de_respuestas(pregunta)

while not contesto:
    print(f"{pregunta["pregunta"]}")

    for k in range(len(respuestas)):
        print(f"{k+1}. {respuestas[k]}")

    ingreso = input("Ingrese 1, 2, 3 o 4 para elegir su opción: ")
    mensaje, valido = verificar_respuesta_correcta(ingreso, respuestas, verdadera)

    if valido:
        print(mensaje)
        contesto = True
        if "correcta" in mensaje.lower():
            correctas += 1
        else:
            incorrectas += 1
    else:
        print(mensaje)

mostrar_resultados(correctas, incorrectas)

