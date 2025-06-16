import random

def randomisar_listas_de_respuestas(diccionario:dict):
    
    verdadera = diccionario["res_correcta"][0]
    falsa_1 , falsa_2 , falsa_3 = diccionario["res_incorrecta"][0],diccionario["res_incorrecta"][1],diccionario["res_incorrecta"][2]

    lista_temp = [verdadera,falsa_1,falsa_2,falsa_3]
    random.shuffle(lista_temp)
    return lista_temp,verdadera


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

    ingreso = int(input("ingrese 1,2,3 o 4 para elegir su opcion elegida: "))

    ingreeso = ingreso - 1

    if 4 >= ingreso >= 1:
        if respuestas[ingreeso] == verdadera:
            print("correcta!")
            contesto = True

        else:
            print("incorrecta")
            contesto = True
    else:
        print("ingreso incorrecto, intente de nuevo")

