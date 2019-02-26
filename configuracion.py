from collections import namedtuple

TAMANNO_LETRA = 30

ANCHO_COL = TAMANNO_LETRA+20
ANCHO_FIL = TAMANNO_LETRA+10

FILAS = 2
COLUMNAS = 20

ANCHO = (COLUMNAS+20) * ANCHO_COL
ALTO = 2* (FILAS+3) * ANCHO_FIL

PISO = ALTO#-2*FILAS


## en segundos
TIEMPO_MAX = 61

INTENTOS_INICIALES = 5

# Frames per second, un frame cada 1/FPS segundos
FPS_inicial = 8


# Colores
COLOR_LETRAS = (200,20,20)
COLOR_TEXTO = (0,0,0)
COLOR_TIEMPO_FINAL = (200,20,10)
COLOR_RESALTADO = (200,20,15)
Punto = namedtuple('Punto','x y')
