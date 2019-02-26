import pygame
from pygame.locals import *
from configuracion import *

def ShowDireccion(direccion):
    if direccion == [-1,-1]:
        return "Abajo - izquierda"
    if direccion == [-1,0]:
        return "Abajo"
    if direccion == [-1,1]:
        return "Abajo - derecha"
    if direccion == [0,-1]:
        return "Izquierda"
    if direccion == [0,0]:
        return "<con el cursor> (8 dir)"
    if direccion == [0,1]:
        return "Derecha"
    if direccion == [1,-1]:
        return "Arriba - izquierda"
    if direccion == [1,0]:
        return "Arriba"
    if direccion == [1,1]:
        return "Arriba - derecha"

def LetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
#    elif key == K_SPACE:
#        return(" ")
    else:
        return("")

## Esta funcion es opcional, sirve para debugging
def PrintMatriz(M, filas):
    for i in range(filas):
        print (M[i])
    print()

## Es opcional usar esta funcion
def escribirEnPantalla(screen, palabra, posicion, tamano, color):
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), tamano)
    ren = defaultFont.render(palabra, 1, color)
    screen.blit(ren, posicion)

def dibujar(screen, candidata, letras, posiciones, puntos, segundos):
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), 20)

    #Linea del piso
    pygame.draw.line(screen, (255,255,255), (0, ALTO-70) , (ANCHO, ALTO-70), 5)

    ren1 = defaultFont.render(candidata, 1, COLOR_TEXTO)
    ren2 = defaultFont.render("Puntos: " + puntos, 1, COLOR_TEXTO)
    if segundos<15 :
        ren3 = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren3 = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)

    for i in range(len(letras)):
        screen.blit(defaultFont.render(letras[i], 1, COLOR_LETRAS), posiciones[i])

    screen.blit(ren1, (190, 570))
    screen.blit(ren2, (680, 10))
    screen.blit(ren3, (10, 10))

def PosicionEnRango(fil, col):
    return (0 <= fil) and (fil <= FILAS) and (0 <= col) and (col <= COLUMNAS)

### "Coordenadas gordas"
def dibujarMatriz(screen, MatLetras, puntos, intentos, palabra, fil, col, direccion, ganador, segundos, inputField):
    defaultFont= pygame.font.Font(pygame.font.get_default_font(), TAMANNO_LETRA)
    #dibuja grilla
    bordeDerecha = (COLUMNAS+0.4) * ANCHO_COL
    for i in range(FILAS):
        coordY = PISO - i * ANCHO_FIL
        pygame.draw.line(screen, (0,0,0), (0, coordY), (bordeDerecha, coordY), 3)
        coordY -= ANCHO_FIL
        pygame.draw.line(screen, (0,0,0), (0, coordY), (bordeDerecha, coordY), 3)

    for j in range(COLUMNAS):
        coordX = j * ANCHO_COL
        pygame.draw.line(screen, (0,0,0), (coordX, coordY), (coordX, PISO), 3)
        coordX -= ANCHO_FIL
        pygame.draw.line(screen, (0,0,0), (bordeDerecha, coordY), (bordeDerecha, PISO), 3)


    ren1a = defaultFont.render("Puntos: " + puntos, 1, COLOR_TEXTO)
    ren1b = defaultFont.render("Intentos disponibles: " + str(intentos), 1, COLOR_TEXTO)
    ren2 = defaultFont.render(ganador, 1, COLOR_TEXTO)

    for i in range(FILAS):
        for j in range(COLUMNAS):
            if MatLetras[i][j] != 0 :
                aux = str(MatLetras[i][j])
            else:
                aux = " "
            screen.blit(defaultFont.render(aux, 1, COLOR_LETRAS),
                        ((j+0.4) * ANCHO_COL, PISO - (i+1) * ANCHO_FIL))

    if inputField == -1:
        screen.blit(defaultFont.render("Intenta de nuevo!", 1, COLOR_RESALTADO), (bordeDerecha / 2, ALTO / 2 - ANCHO_FIL))
    if inputField == 0:
        color3a = COLOR_RESALTADO
        color3b = COLOR_TEXTO
        color3c = COLOR_TEXTO
        color3d = COLOR_TEXTO
    elif inputField == 1:
        color3a = COLOR_TEXTO
        color3b = COLOR_RESALTADO
        color3c = COLOR_TEXTO
        color3d = COLOR_TEXTO
    elif inputField == 2:
        color3a = COLOR_TEXTO
        color3b = COLOR_TEXTO
        color3c = COLOR_RESALTADO
        color3d = COLOR_TEXTO
    elif inputField == 3:
        color3a = COLOR_TEXTO
        color3b = COLOR_TEXTO
        color3c = COLOR_TEXTO
        color3d = COLOR_RESALTADO

    if(fil!=""):
        f = int(fil)
    else:
        f=-2
    if(col!=""):
        c = int(col)
    else:
        c=-2


    if PosicionEnRango(f,c):
            screen.blit(defaultFont.render(str(MatLetras[f][c]), 1, COLOR_RESALTADO),
                       ((c+0.4) * ANCHO_COL, PISO - (f+1) * ANCHO_FIL))
    else:
        color3a = COLOR_TEXTO
        color3b = COLOR_TEXTO
        color3c = COLOR_TEXTO
        color3d = COLOR_TEXTO


    ren3a = defaultFont.render("Palabra: " + palabra, 1, color3a)
    #ren3b = defaultFont.render("Fila: " + fil, 1, color3b)
    #ren3c = defaultFont.render("Columna: " + col, 1, color3c)
    #ren3d = defaultFont.render("Direccion: " + direccion, 1, color3d)
    ren6 = defaultFont.render("Intentos Disponibles: " + str(intentos), 1, COLOR_TEXTO)
    if intentos==0 or segundos<=0:
		# CAMBIAR POR ALGO MAS LINDO
        ren4 = defaultFont.render("Perdiste... Presiona S para salir", 1,(200,10,10))
        screen.blit(ren4, (ANCHO_COL, ALTO / 2 + ANCHO_FIL))

    if segundos<15:
        color9 = COLOR_TIEMPO_FINAL
    else:
        color9 = COLOR_TEXTO
    ren9 = defaultFont.render("Tiempo: " + str(int(segundos)), 1, color9)


    screen.blit(ren1a, (ANCHO_COL, 10))
    screen.blit(ren1b, (ANCHO_COL, 10 + ANCHO_FIL))
    screen.blit(ren2, (ANCHO_COL, PISO + ANCHO_FIL * 5/3))
    screen.blit(ren3a, (ANCHO_COL, ALTO / 2))
#    screen.blit(ren4, (ANCHO_COL, ALTO / 2 + ANCHO_FIL))
#    screen.blit(ren3c, (bordeDerecha + ANCHO_COL, ALTO / 2 + 2* ANCHO_FIL))
#    screen.blit(ren3d, (bordeDerecha + ANCHO_COL, ALTO / 2 + 3* ANCHO_FIL))
    screen.blit(ren9, (bordeDerecha / 2, 10))
