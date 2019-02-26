#############################################################################################################

        # Menu principal y opciones -

#############################################################################################################
import extras
import juego
import pygame
import dumbmenu as dm
import os
from pygame.locals import *

# Variables
rojo = (255,0,0)
negro = (0,0,0)
dificultad = 1
tematica = 0

def menu_principal():
  #Se centra la ventana, se inicializa la musica, el fondo, el nombre mostrado en la parte superior de la ventana y su tamaÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â±o.
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    pygame.mixer.init()
    sonidoMenu = pygame.mixer.Sound("pageturn.wav")
    pygame.display.set_caption("MEZCLA PALABRAS")
    screen = pygame.display.set_mode((900,650))#((ANCHO, ALTO))#
    ImagenFondo=pygame.image.load("ventana_menu.png").convert()
    screen.blit (ImagenFondo, (0, 0))
    pygame.mixer.music.load("title.mid")
    pygame.mixer.music.play()
    #titulo
    t= pygame.font.Font("arhermann.ttf",90)
    ren = t.render("Mezcla Palabras", 0, negro)
    screen.blit(ren,(120,170))
    #Se actualiza la pantalla
    pygame.display.update()
    pygame.key.set_repeat(500,30)
    #Se crea el menu y redirecciona segun la opcion elegida.-
    choose = dm.dumbmenu(screen, ['Jugar','Opciones','Salir'], 310,364,None,70,1.4,negro,rojo)
    if choose == 0:
      #print ("Elegiste Jugar")
      sonidoMenu.play(0)
      Img=pygame.image.load("ventana.png").convert()
      screen.blit (Img, (0, 0))
      extras.escribirEnPantalla(screen, "ADIVINA LA MAYOR CANTIDAD DE PALABRAS POSIBLE", (100,150), 25, negro)
      extras.escribirEnPantalla(screen, "          Y CONSIGUE EL MAYOR PUNTAJE !      ", (100,200), 25, negro)
      pygame.display.update()
      juego.main(screen,dificultad,tematica)

    elif choose == 1:
      #print ("Elegiste 'Opciones'.")
      sonidoMenu.play(0)
      menu_opciones(screen)
    #elif choose == 2:
      #print ("Elegiste 'Ranking'.")
      #sonidoMenu.play(0)
      #return()
    elif choose == 2:
      #print ("Elegiste 'Salir'.")
      pygame.quit()
      return


def menu_opciones(screen):
    #Como recibe de parametro screen las lineas que siguen son para debug./
    #pygame.display.set_caption("Mezcla Palabras")
    #size = width, height = 900,650
    #screen = pygame.display.set_mode(size)
    ImagenFondo=pygame.image.load("ventana_menu.png").convert()
    screen.blit (ImagenFondo, (0, 0))
    pygame.display.update()
    choose = dm.dumbmenu(screen, ['Dificultad','Tematica','Volver'], 310,364,None,70,1.4,negro,rojo)
    sonidoMenu = pygame.mixer.Sound("pageturn.wav")
    if choose == 0:
      #print ("Elegiste 'Dificultad'.")
      sonidoMenu.play(0)
      menu_dificultad(screen)

    elif choose == 1:
      #print ("Elegiste 'Tematica'.")
      sonidoMenu.play(0)
      menu_tematica(screen)

    elif choose == 2:
      #print ("Elegiste 'Volver'.")
      sonidoMenu.play(0)
      menu_principal()

def menu_dificultad(screen):
    global dificultad
    #Como recibe de parametro screen las lineas que siguen son para debug./
    #pygame.display.set_caption("Mezcla Palabras")
    #size = width, height = 900,650
    #screen = pygame.display.set_mode(size)
    ImagenFondo=pygame.image.load("ventana_menu.png").convert()
    screen.blit (ImagenFondo, (0, 0))
    pygame.display.update()
    sonidoMenu = pygame.mixer.Sound("pageturn.wav")
    choose = dm.dumbmenu(screen, ['Facil','Normal','Dificil'], 310,364,None,70,1.4,negro,rojo)

    if choose == 0:
      #print ("Elegiste 'Facil'.")
      sonidoMenu.play(0)
      dificultad = 0
      menu_principal()

    elif choose == 1:
      #print ("Elegiste 'Normal'.")
      sonidoMenu.play(0)
      dificultad = 1
      menu_principal()

    elif choose == 2:
      #print ("Elegiste 'Dificil'.")
      sonidoMenu.play(0)
      dificultad = 2
      menu_principal()

def menu_tematica(screen):
    global tematica
    #Como recibe de parametro screen las lineas que siguen son para debug./
    #pygame.display.set_caption("Mezcla Palabras")
    #size = width, height = 900,650
    #screen = pygame.display.set_mode(size)
    ImagenFondo=pygame.image.load("ventana_menu.png").convert()
    screen.blit (ImagenFondo, (0, 0))
    pygame.display.update()
    sonidoMenu = pygame.mixer.Sound("pageturn.wav")
    choose = dm.dumbmenu(screen, ['Sustantivos','Verbos','Adjetivos'], 310,364,None,70,1.4,negro,rojo)

    if choose == 0:
      #print ("elegiste la lista de Sustantivos")
      sonidoMenu.play(0)
      tematica = 0
      menu_principal()

    elif choose == 1:
      #print ("elegiste la lista de Verbos")
      sonidoMenu.play(0)
      tematica = 1
      menu_principal()
    elif choose == 2:
      #print ("elegiste la lista de Adjetivos")
      sonidoMenu.play(0)
      tematica = 2
      menu_principal()

menu_principal()