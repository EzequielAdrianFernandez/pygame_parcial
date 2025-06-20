from usuarios import *
'''
la biblioteca tiene este molde:



biblioteca_usuarios = {
    "usuario_1": {
        "nombre": "pachacho",
        "record_boletos": 15,       # Mayor cantidad de boletos en una partida
        "total_boletos": 87,       # Acumulado histórico de boletos
        "partidas_jugadas": 12     # Partidas completadas
    },
    "usuario_2": {
        "nombre": "pachacha",
        "record_boletos": 23,
        "total_boletos": 156,
        "partidas_jugadas": 20
    }
}



'''
##########################################################################################################################################################################


def registrar_puntaje(puntaje_positivo:int,puntaje_negativo:int,usuario:str,dificultad:str):

    if dificultad == "facil":
        bonificador_de_dificultad = 1
    elif dificultad == "medio":
        bonificador_de_dificultad = 3
    elif dificultad == "dificil":
        bonificador_de_dificultad = 5

    puntaje_nuevo = (puntaje_positivo + puntaje_negativo)*bonificador_de_dificultad
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





def mostrar_resultados_partida_actual(correctas: int, incorrectas: int,tickets_conseguidos):
    print("\n--- RESULTADOS DE PARTIDA ---")
    print(f"Respuestas correctas: {correctas}")
    print(f"Respuestas incorrectas: {incorrectas}")
    print(f"tickets conseguidos: {tickets_conseguidos}")
