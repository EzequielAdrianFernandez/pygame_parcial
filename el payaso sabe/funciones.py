import random 

def randomisar_listas_de_respuestas(diccionario:dict):
    
    verdadera =str(diccionario["res_correcta"][0])
    falsa_1 , falsa_2 , falsa_3 = diccionario["res_incorrecta"][0],diccionario["res_incorrecta"][1],diccionario["res_incorrecta"][2]

    lista_temp = [verdadera,falsa_1,falsa_2,falsa_3]
    lista_temp = random.shuffle(lista_temp)
    return lista_temp,verdadera



def verificar_respuesta_correcta(ingreso:str,respuestas_mezcladas:list,res_correcta:str):
    numeros_validos = ["1","2","3","4"]
    invalidas = 0

    for m in range(len(numeros_validos)):

        if ingreso == numeros_validos[m]:
            ingreso_int=int(ingreso)
            ingreso_int = ingreso_int - 1
            contesto = True

            if respuestas_mezcladas[ingreso_int] == res_correcta:
                return "correcta!",contesto

            else:
                return "incorrecta :(",contesto

        else:
            invalidas += 1

        if invalidas == 4:
            contesto = False
            return "ingreso invalido",contesto



def randomisar_listas_de_respuestas(diccionario:dict):
    
    verdadera = diccionario["res_correcta"][0]
    falsa_1 , falsa_2 , falsa_3 = diccionario["res_incorrecta"][0],diccionario["res_incorrecta"][1],diccionario["res_incorrecta"][2]

    lista_temp = [verdadera,falsa_1,falsa_2,falsa_3]
    random.shuffle(lista_temp)
    return lista_temp,verdadera

