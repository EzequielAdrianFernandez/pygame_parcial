import random
from funciones_bis import *
from base_de_datos_bis import *


contesto = False

dificultades=["facil","facil","facil","medio","medio","medio","dificil","dificil","dificil",]

seguir_jugando = True
aciertos = 0
fallas = 0
ronda = 1
tickets_conseguidos = 0
while seguir_jugando:
    limite = 8
    if ronda == limite:
        seguir_jugando = False

    dificultad = dificultades[ronda]
    categoria , pregunta = seleccionar_pregunta(biblioteca_preguntas,dificultad)

    respuestas , verdadera = randomisar_listas_de_respuestas(pregunta)


    while not contesto:
        print(f"{pregunta["pregunta"]}")

        for k in range(len(respuestas)):
            print(f"{k+1}. {respuestas[k]}")

        ingreso = input("Ingrese 1, 2, 3 o 4 para elegir su opción: ")
        mensaje, valido, tickets_ronda = verificar_respuesta_correcta(ingreso, respuestas, verdadera ,dificultad )

        if valido:
            
            contesto = True
            if mensaje == "¡Correcta!":
                aciertos += 1
                tickets_conseguidos = tickets_conseguidos + tickets_ronda
            else:
                fallas += 1
            print(mensaje)
            mostrar_resultados_ronda(tickets_ronda)
            
        else:
            print(mensaje)
    
    contesto = False
    ronda += 1
mostrar_resultados_partida(aciertos,fallas,tickets_conseguidos)
