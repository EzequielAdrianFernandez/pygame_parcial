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





def agregar_usuario_auto(nombre):
    nuevo_id = f"usuario_{len(biblioteca_usuarios) + 1}"
    biblioteca_usuarios[nuevo_id] = {
        "nombre": nombre,
        "record_boletos": 0,
        "total_boletos": 0,
        "partidas_jugadas": 0
    }
    return nuevo_id