
import random 
import base_de_datos_bis


def seleccionar_pregunta(biblioteca, dificultad:str):
    categoria = random.choice(list(biblioteca.keys()))
    pregunta = random.choice(biblioteca[categoria][dificultad])
    return categoria, pregunta


def verificar_respuesta_correcta(ingreso: str, respuestas_mezcladas: list, res_correcta: str):
    if ingreso in ["1", "2", "3", "4"]:
        index = int(ingreso) - 1
        if respuestas_mezcladas[index] == res_correcta:
            return " ¡Correcta!", True
        else:
            return " Incorrecta.", True
    else:
        return " Ingreso inválido", False


def mostrar_resultados(correctas: int, incorrectas: int):
    print("\n--- RESULTADOS FINALES ---")
    print(f"Respuestas correctas: {correctas}")
    print(f"Respuestas incorrectas: {incorrectas}")


import random
def randomisar_listas_de_respuestas(diccionario: dict):
    verdadera = diccionario["respuestas"]["correcta"]  # Cambiado a "correcta"
    lista_temp = [verdadera] + diccionario["respuestas"]["incorrectas"]  # Cambiado a "incorrectas"
    random.shuffle(lista_temp)
    return lista_temp, verdadera