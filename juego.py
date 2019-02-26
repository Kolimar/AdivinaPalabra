#! /usr/bin/env python
import os, random, sys, math
import pygame
from pygame.locals import *
from configuracion import *
from funciones import *
from extras import *
#############################################################################################################

        # Funcion main con el juego./

#############################################################################################################

def main(screen,dificultad,tematica):
    # Recibo como parametro la pantalla donde correra el juego. pygame.display.set_mode((ANCHO, ALTO))
    # las proximas 2 lineas serian para debug y tests, por lo que estan comentadas./
    #pygame.display.set_caption("MEZCLA PALABRAS")
    #screen = pygame.display.set_mode((900,650))#((ANCHO, ALTO))
    #tiempo total del juego
    gameClock = pygame.time.Clock()
    totaltime = 0
    segundos = TIEMPO_MAX
    segundos2 = TIEMPO_MAX + pygame.time.get_ticks()/1000
    fps = FPS_inicial
    #Inicializo el archivo con palabras lo guardo en una variable, elijo una palabra y creo una lista con sus caracteres en una variable.
    #Filtro por dificultad.-
    lemario = DificultadElegida(dificultad,InitLemario(tematica))
    palabraLista = PalabraALista(EligePalabra(lemario))
    #Creo una Matriz con (filas)listas de (columnas)largo.-
    mat = [ ["" for j in range(COLUMNAS)] for i in range(FILAS)]
    #Genero la tira de letras desordenadas y las que se van ordenando cada 10s.-
    InitMat(mat,palabraLista)
    ganador = ""
    puntos = 0
    intentos = INTENTOS_INICIALES
    salieron = []
    ##
    ImagenFondo=pygame.image.load("ventana.png").convert()
    #inputField
    #  0: palabra
    #  1: fila
    #  2: columna
    #  3: direccion
    inputField = 0
    palabra = ""
    fil = col = ""
    direccion = [0,0]
    showDireccion = ""
    #cargo los sonidos en variables.-
    sonidoAcierto = pygame.mixer.Sound("correct.wav")
    sonidoError = pygame.mixer.Sound("wrong.wav")

 #Dibujo la matriz, asigno fuente.
    dibujarMatriz(screen, mat, "0", intentos, palabra, fil, col, "", ganador, segundos, inputField)

#Mientras los segundos sean mayores a 0 y los intentos tambien...
    while segundos > fps/1000 and intentos>0:
        # 1 frame cada 1/fps segundos
        gameClock.tick(fps)
        totaltime += gameClock.get_time()

        if True:
            fps = 3

        #Buscar la tecla apretada del modulo de eventos de pygame
        for e in pygame.event.get():

            #QUIT es apretar la X en la ventana
            if e.type == QUIT:
                pygame.quit()
                return()

            #Ver si fue apretada alguna tecla
            if e.type == KEYDOWN:
                #Ingresar palabra
                if inputField < 1:
                    letra = LetraApretada(e.key)
                    palabra += letra
                    if e.key == K_BACKSPACE:
                        palabra = palabra[0:len(palabra)-1]
                    if e.key == K_RETURN and palabra != "":
                        inputField = 1

        if inputField == 1:
            if PalabraCorrecta(palabra,palabraLista):
                puntos += Puntos(palabra)
                inputField = 0
                salieron.append(palabra)
                palabraLista = PalabraALista(EligePalabra(lemario))
                mat = [ ["" for j in range(COLUMNAS)] for i in range(FILAS)]
                InitMat(mat,palabraLista)
                #agrego un sonido de acierto sin repeticion, y uno de error al caso contrario.-
                sonidoAcierto.play(0)
            else:
                inputField = -1
                intentos -= 1
                sonidoError.play(0)
            palabra = ""
            fil = col = ""
            direccion = [0,0]
            showDireccion = ""

        segundos = segundos2 - pygame.time.get_ticks()/1000

        #Limpiar pantalla anterior
        screen.blit (ImagenFondo, (0, 0))

        if int(segundos)%10 == 0 and int(segundos) != 0: #Renueva la matriz cada 10 segundos
            print(palabraLista)
            OrdenaLetra(mat,palabraLista)
            pygame.time.wait(1000)

        #Dibujar de nuevo todo
        dibujarMatriz(screen, mat, str(puntos), intentos, palabra, fil, col, ShowDireccion(direccion), ganador, segundos, inputField)


        pygame.display.flip()

    pygame.mixer.music.load("fast.mp3")
    pygame.mixer.music.play()
    pygame.display.update()
    while 1:
            #Esperar el QUIT del usuario
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                return
            elif e.key == K_s:
                pygame.quit()
                return
#para inicializar el juego sin menu descomentar las siguientes lineas, y las lineas 18 y 19 de main. dif 0,1,2 tematica, 0,1,2.
#dificultad = 1
#tematica = 0
#main(screen, dificultad,tematica)