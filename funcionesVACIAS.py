from principal import *
from configuracion import *

import random
import math


def cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer):           ##funciona por el momento
    #elige una palabra de la lista y la carga en las 3 listas
    # y les inventa una posicion para que aparezca en la columna correspondiente

    ANCHO=600
    ALTO=800
    palabra_random= random.choice(lista)

##    coordenadas = coordenadas
##
    global coordenadas
    global pos_x
    global pos_y

    for palabra in lista:
        if palabra == palabra_random:
         for letra in palabra:

            pos_x= random.randrange(0,ANCHO)

            pos_y = random.randrange(0,ALTO-70)

            coordenadas = [pos_x,pos_y]
            

            if pos_x <= (ANCHO-400):

                listaIzq.append (letra)
                posicionesIzq.append (coordenadas)
                return coordenadas

            else:
                if pos_x <= (ANCHO-200):

                    listaMedio.append (letra)
                    posicionesMedio.append (coordenadas)
                    return coordenadas

                else:
                    if pos_x <= (ANCHO):

                        listaDer.append (letra)
                        posicionesDer.append (coordenadas)
                        return coordenadas



         return posicionesIzq, posicionesMedio, posicionesDer




#pp

##lista=["Argentina", "Uruguay", "Brasil"]
##listaIzq=[]
##listaMedio=[]
##listaDer=[]
##posicionesIzq=[]
##posicionesMedio=[]
##posicionesDer=[]
##
##print (cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer))



#-------------------------------------------------------------------------------
def bajar(lista, posiciones):               ##falta agregar la funcion  cargarLista para que las letras se carguen mientras bajan las letras de posicion
                                            ## falta realizar bien el recorrido de una letra por el eje y
# hace bajar las letras y elimina las que tocan el piso

    ANCHO=600
    ALTO=800
    
    cont = 0

    while cont <= TIEMPO_MAX:
        cont = cont + 1
                

   
##        #------------------------------------------
##    for letra in cargarLista(posicionesMedio):
##
##
##            while coordenadas[1] < (ALTO-70):
##
##                 coordenadas[1] =coordenadas[1] + 10
##
##            return coordenadas
##
##        #-----------------------------------------
##    for letra in cargarLista(posicionesDer):
##
##
##            while coordenadas[1] < (ALTO-70):
##
##                 coordenadas[1] = coordenadas[1] + 10
##
##            return coordenadas



#elimina las que tocan el suelo

##    if coordenadas[1] >= (ALTO - 70):
##
##            listabasura.pop(coordenadas)
##
##            return listabasura
##
##
##
###recorre lista por lista para asignarle que baje por el eje y aumentadolo
##    ANCHO=600
##    ALTO=800
##
##    for elem in lista:
##        for letra in elem:
##
##            posi_x = random.randrange(0,ANCHO)
##            posi_y = 0
##
##            posiciones =[posi_x,posi_y]
##
##            while posiciones[1] < (ALTO-70):
##
##                 posiciones[1] = posiciones[1] + 10
##
##            return posiciones

###elimina las que tocan el suelo
##            if posiciones[1] >= (ALTO - 70):
##
##                listabasura.pop(coord)
##
##                return listabasura


###pp
##listabasura=[]
##lista=["Argentina", "Brasil", "Bolivia"]
##posiciones=[]
##print (bajar(lista,posiciones))



#-------------------------------------------------------------------------------
def actualizar(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer):
    ## llama a otras funciones para bajar bajar las letras, eliminar las que tocan el piso y
    ## cargar nuevas letras a la pantalla (esto puede no hacerse todo el tiempo para que no se llene de letras la pantalla)
    pass
##    TIEMPO_MAX=4
##    lista=lista
##    posicion=[posicionesIzq,posicionesMedio,posicionesDer]
##    bajarse=bajar(lista,posicion)
##    if bajarse==True:
##     tiempo=0
##     while tiempo<TIEMPO_MAX:
##        tiempo+=1
##        if tiempo==TIEMPO_MAX:
##         cargarListas=(lista,listaIzq,listaMedio,listaDer,posicionesIzq,posicionesMedio,posicionesDer)
##         return cargarListas



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

    p=0

    for letra in candidata:
        if letra in vocales:
            p += 1
        else:
            if letra in consonantes:
                p += 2
            else:
                if letra in con_dificiles:
                    p += 5
    return p



#-------------------------------------------------------------------------------
def procesar(lista, candidata, listaIzq, listaMedio, listaDerecha):
    #chequea que candidata sea correcta en cuyo caso devuelve el puntaje y 0 si no es correcta

    if esValida(lista, candidata, listaIzq, listaMedio, listaDerecha) == True:
        puntos_candidata = Puntos(candidata)
        return puntos_candidata

    else:
        return 0



#-------------------------------------------------------------------------------
def esValida(lista, candidata, listaIzq, listaMedio, listaDerecha):           ##falta cambiar algo para que tome el puntaje
    #devuelve True si candidata cumple con los requisitos
    valida=False

    archivo = open("nombre_lista.txt","r", encoding="utf-8")
    nombre_lista=archivo.readlines()
    archivo.close()
    for elem in lista:
        if elem in nombre_lista:
            valida = True


