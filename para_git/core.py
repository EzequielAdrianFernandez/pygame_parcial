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
no_coincide = 0

while contesto == False:

    print(f"{biologia["pregunta"]}:")

    for k in range(len(respuestas)):
        print(f"{respuestas[k]}")

    ingreso =(input("ingrese 1,2,3 o 4 para elegir su opcion elegida: "))

    numeros_validos = ["1","2","3","4"]

    for m in range(len(numeros_validos)):
        if ingreso == numeros_validos[m]:
            ingreeso=int(ingreso)
            ingreeso = ingreeso - 1


            if respuestas[ingreeso] == verdadera:
                print("correcta!")
                contesto = True

            else:
                print("incorrecta :(")
                contesto = True

        else:
            no_coincide += 1

        if no_coincide == 4:
            print("ingreso incorrecto, intente de nuevo")
