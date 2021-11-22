from principal import *
from configuracion import *

import random
import math


##################################################
############Funciones Auxiliares####################
def esta(elem,lista):
    for letra in lista:
        if letra==elem:
            return True
#################################################

def cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer):           ##funciona por el momento
    #elige una palabra de la lista y la carga en las 3 listas
    # y les inventa una posicion para que aparezca en la columna correspondiente

    ANCHO = 800
    ALTO = 600
    palabra_random = random.choice(lista)


    for palabra in lista:
        if palabra == palabra_random:
         for letra in palabra:

            coordenadas = [random.randrange(0,ANCHO-10),random.randrange(0,ALTO-70)]

            if coordenadas[0] <= ANCHO-550 and coordenadas[1] <= ALTO-100:

                listaIzq.append (letra)
                posicionesIzq.append (coordenadas)


            else:
                if coordenadas[0] <= ANCHO-265 and coordenadas[1] <= ALTO-100:

                    listaMedio.append (letra)
                    posicionesMedio.append (coordenadas)


                else:
                    if coordenadas[0] <= ANCHO-1 and coordenadas[1] <= ALTO-100:

                        listaDer.append (letra)
                        posicionesDer.append (coordenadas)





#-------------------------------------------------------------------------------
def bajar(lista, posiciones):               ##falta agregar la funcion  cargarLista para que las letras se carguen mientras bajan las letras de posicion
                                            ## falta realizar bien el recorrido de una letra por el eje y
# hace bajar las letras y elimina las que tocan el piso

    ANCHO=600
    ALTO=800
    
    cont = 0

    while cont <= TIEMPO_MAX:
        cont = cont + 1
                



#-------------------------------------------------------------------------------
def actualizar(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer):
    ## llama a otras funciones para bajar bajar las letras, eliminar las que tocan el piso y
    ## cargar nuevas letras a la pantalla (esto puede no hacerse todo el tiempo para que no se llene de letras la pantalla)

    bajar(listaIzq, posicionesIzq)
    bajar(listaMedio, posicionesMedio)
    bajar(listaDer, posicionesDer)
    cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer)
    pass





#-------------------------------------------------------------------------------
def estaCerca(elem, lista):
    #es opcional, se usa para evitar solapamientos
    pass



#-------------------------------------------------------------------------------
def Puntos(candidata):
    #devuelve el puntaje que le corresponde a candidata

    vocales= "aeiouAEIOU"
    consonantes="bcdfghlmnñprstvBCDFGJHLMNÑPRSTV"
    con_dificiles="jkqwxyzJKQWXYZ"

    puntaje=0

    for letra in candidata:
        if letra in vocales:
            puntaje += 1
        else:
            if letra in consonantes:
                puntaje += 2
            else:
                if letra in con_dificiles:
                    puntaje += 5

    return puntaje
    pass



#-------------------------------------------------------------------------------
def procesar(lista, candidata, listaIzq, listaMedio, listaDerecha):
    #chequea que candidata sea correcta en cuyo caso devuelve el puntaje y 0 si no es correcta

    if esValida(lista, candidata, listaIzq, listaMedio, listaDerecha) == True:
        puntos_candidata = Puntos(candidata)
        return puntos_candidata

    else:
        return 0
    pass




#-------------------------------------------------------------------------------
def esValida(lista, candidata, listaIzq, listaMedio, listaDerecha):           ##falta cambiar algo para que tome el puntaje
    #devuelve True si candidata cumple con los requisitos
    valida=False
    for palabrasA in lista:
       if palabrasA in candidata:
        valida=True
       else:
          I=esta(candidata, listaIzq)
          if I==True:
            valida=True
          M=esta(candidata, listaMedio)
          if M==True:
            valida=True
          D=esta(candidata, listaDerecha)
          if D==True:
            valida=True
    return valida
    ##(Si candidata no esta en lista) Busco si candidata esta en las listasizq, media y derecha, si esto se cumple lista es valida
    pass



