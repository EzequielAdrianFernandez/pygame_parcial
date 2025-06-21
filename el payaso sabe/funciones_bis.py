
import random 
from base_de_datos_bis import*

def seleccionar_pregunta(biblioteca, dificultad:str):
    categoria = random.choice(list(biblioteca.keys()))
    pregunta = random.choice(biblioteca[categoria][dificultad])
    return categoria, pregunta






def verificar_respuesta_correcta(ingreso: str, respuestas_mezcladas: list, res_correcta: str,dificultad:int):
    if dificultad == "facil":
        tickets = 1
    elif dificultad == "medio":
        tickets = 3
    elif dificultad == "dificil":
        tickets = 5
    else:
        tickets = None

    if ingreso in ["1", "2", "3", "4"]:
        index = int(ingreso) - 1
        if respuestas_mezcladas[index] == res_correcta:
            return "¡Correcta!", True , tickets
        else:
            return " Incorrecta.", True , 0
    else:
        return " Ingreso inválido", False , None




import random
def randomisar_listas_de_respuestas(diccionario: dict):
    verdadera = diccionario["respuestas"]["correcta"] 
    lista_temp = [verdadera] + diccionario["respuestas"]["incorrectas"]  
    random.shuffle(lista_temp)
    return lista_temp, verdadera






def agregar_usuario_auto(nombre):
    nuevo_id = f"usuario_{len(biblioteca_usuarios) + 1}"
    biblioteca_usuarios[nuevo_id] = {
        "nombre": nombre,
        "record_boletos": 0,
        "total_boletos": 0,
        "partidas_jugadas": 0
    }
    return nuevo_id







def mostrar_resultados_ronda(tickets_conseguidos):
    print("---TICKETS CONSEGUIDOS---")
    print("con esta pregunta conseguiste:")
    print(f"{tickets_conseguidos} ticket(s)")

def registrar_puntaje_partida(tickets_conseguidos,usuario:str):

    puntaje_nuevo = tickets_conseguidos
    if puntaje_nuevo > biblioteca_usuarios[usuario]["record_boletos"]:
        biblioteca_usuarios[usuario]["record_boletos"] = puntaje_nuevo
        print(f"¡Nuevo récord! {usuario}: {puntaje_nuevo} boletos")
        biblioteca_usuarios[usuario]["partidas_jugadas"] += 1
    biblioteca_usuarios[usuario]["total_boletos"] += puntaje_nuevo






def mostrar_estadisticas(id_usuario):
    if id_usuario in biblioteca_usuarios:
        stats = biblioteca_usuarios[id_usuario]
        print(f"""
    │  ESTADÍSTICAS DE {stats['nombre'].upper():<25}│
    │  • Récord: {stats['record_boletos']:<5} boletos (1 partida)  │
    │  • Total acumulado: {stats['total_boletos']:<5} boletos      │
    │  • Partidas jugadas: {stats['partidas_jugadas']:<5}          │
        """)
    else:
        print(f"Error: El usuario '{id_usuario}' no existe.")






def mostrar_resultados_partida(correctas: int, incorrectas: int, tickets_conseguidos: int):
    """
    Muestra los resultados de la partida actual con formato mejorado
    
    Args:
        correctas (int): Número de respuestas correctas
        incorrectas (int): Número de respuestas incorrectas
        tickets_conseguidos (int): Tickets obtenidos en la partida
    """
    total_preguntas = correctas + incorrectas
    porcentaje_acierto = (correctas / total_preguntas * 100) 
    
    print("========================================")
    print(" RESULTADOS DE LA PARTIDA ")
    print("========================================")
    print(f" ✔ Correctas: {correctas} ({porcentaje_acierto:.1f}%)")
    print(f" ✖ Incorrectas: {incorrectas}")
    print(f" 🎫 Tickets ganados: {tickets_conseguidos}")
    print("========================================")
    





