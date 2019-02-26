# AdivinaPalabra

Introduccion a la programacion Mezcla Palabras
May 7, 2015
Introduccion
El trabajo consiste en implementar un juego para ordenar palabras, cuyo objetivo es adivinar la palabra cuyas letras que aparecen mezcladas en la pantalla. Gran parte del juego ya esta hecha, solamente falta implementar las funcionalidades mas importantes.
1 El Juego de las palabras
Reglas del Juego
Se juega de a un jugador, que cuenta con 60 segundos para adivinar la palabra desordenada que esta´ en pantalla. El jugador debe escribir la palabra en pantalla y si la palabra es la correcta en castellano, se deben sumar puntos al jugador y aparece una nueva palabra. Si es incorrecta la palabra, el jugador pierde una vida (intentos fallidos) de un total de cinco. Cada 10 segundos aparece una letra de la palabra en el orden correcto como ayuda.
Lo que ya esta implementado
El juego actualmente consta de un archivo con el programa principal. Este se encarga de capturar la entrada del teclado, llevar la cuenta de los puntos y del tiempo, as´ı como tambi´en de dibujar en la pantalla. El programa principal cuenta tambi´en con:
• una variable de tipo lista que es una matriz que guarda las letras que esta´n en pantalla.
• una variable de tipo lista que guarda la palabra que hay que adivinar.
Las letras esta´n divididas en 3 grupos, las vocales, las consonantes comunes y las consonantes dif´ıciles que otorgan distintos puntos al formar parte de la palabra que debe adivinar el jugador. El programa toma la palabra al azar desde
1
el lemario donde se encuentran las palabras del castellano y la desordena antes de mostrarla en pantalla, si el jugador ingresa la palabra correcta, la jugada es va´lidas y las letras suman puntos de acuerdo a la clasiﬁcacio´n mencionada. Adema´s, cada 10 segundos una de las letras aparece en forma ordenada como ayuda al jugador.
Para la mayor´ıa de estas tareas, el programa hace uso de una biblioteca de c´odigo llamada PyGame. Una biblioteca de c´odigo es un conjunto de subprogramas utilizados para desarrollar software. En particular PyGame es una biblioteca especialmente disen˜ada para el desarrollo de juegos interactivos en Python.
La posicion (0,0) de la pantalla es el vertice inferior izquierdo, las x crecen hacia la derecha y las y crecen hacia arriba.
