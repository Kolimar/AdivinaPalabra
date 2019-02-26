#from principal import *
from extras import *
from configuracion import *
import random, math

def InitLemario(tematica):#Se le agrego un parametro "tematica", para poder elegirla.
    #Primero se filtra por tematica, se selecciona el archivo de acuerdo a lo seleccionado.-
    if tematica==0:
        archivo=open("sustantivos.txt","r")
        lista=archivo.readlines()
        archivo.close()
    elif tematica==1:
        archivo=open("verbos.txt","r")
        lista=archivo.readlines()
        archivo.close()
    elif tematica==2:
        archivo=open("adjetivos.txt","r")
        lista=archivo.readlines()
        archivo.close()
    nuevaLista=[]
    ultimaCadena=[lista[len(lista)-1]] #saco la ultima palabra del lemario.
    for cadena in lista:
        if cadena != (lista[len(lista)-1]): # recorro hasta la penultima palabra.
           nuevaLista.append(cadena[:-1])  #le saco a las palabras el "/n".
    D=nuevaLista+ultimaCadena        #concateno al lemario la ultima palabra.
    return D

def EligePalabra(lemario):
    #archivo=open("datos.txt","r")
    #lista=archivo.readlines()
    #archivo.close()
    l1=random.choice(lemario) # el ".choice" es una funcion del random para elegir.
    return(l1)

def DificultadElegida(dificultad,lista): #Esta funcion recibe como parametro la dificultad(0,1,2) y la lista de palabras a filtrar.
    #Creo una lista vacia para poder almacenar las palabras filtradas.
    listaPosibles=[]
    if dificultad==0:
        for elemento in lista:
            if len(elemento)<5:
                listaPosibles.append(elemento)
    elif dificultad==1:
        for elemento in lista:
            if len(elemento)<7:
                listaPosibles.append(elemento)
    elif dificultad==2:
        for elemento in lista:
            if len(elemento)>6:
                listaPosibles.append(elemento)
    # para imprimir las palabras guardadas en la lista, descomentar la sigte linea.
    # print (listaPosibles)
    return (listaPosibles)

def PalabraALista(palabra):
    #Se crea una lista vacia y se almacena en una variable, luego se recorre cada letra de la palabra de la funcion
    # se guarda cada letra como un elemento de la lista.-
    caracteres = []
    for char in palabra:
        caracteres+=char
    return(caracteres)

def MezclaLetras(listaPalabra):
    #Creo una lista de posiciones desordenadas.-
    index = []
    for x in range(len(listaPalabra)):
        index.append(x)
    random.shuffle(index)
    #Le asigno a cada posicion una letra de la palabra correspondiente al index desordenado.-
    for i in range (len(listaPalabra)):
        index[i] = listaPalabra[index[i]]
    return(index)


def InitMat(mat,palabraLista):
    #Grabo la lista desordenada.
    i=0
    x = palabraLista
    listaDesordenada=MezclaLetras(x)
    for elemento in listaDesordenada:
        mat[1][i] = elemento
        i=i+1

def OrdenaLetra(mat,palabraLista):
    for i in range (0,len(palabraLista)):
        if not mat[0][i] == palabraLista[i]:
            mat[0][i]=palabraLista[i]
            return()

def PalabraCorrecta(candidata,palabraLista):
    #Se compara la palabra ingresada con la palabra a adivinar.-
    if palabraLista==PalabraALista(candidata):
        return (True)
    else:
        return(False)

def Puntos(candidata):
    #Se suman puntos segun cada letra de la palabra adivinada valga, dif(5),vocal(1),resto(2).-
    puntaje=0
    vocales=["a","e","i","o","u"]
    dificiles=["j","k","q","w","x","y","z"]
    lista = PalabraALista(candidata)
    for elemento in lista:
        if elemento in dificiles:
            puntaje+=5
        elif elemento in vocales:
            puntaje+=1
        else:
            puntaje+=2
    return(puntaje)