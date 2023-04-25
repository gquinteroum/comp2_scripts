#!/usr/bin/python

import sys

# it's easy to print this list of course:
print (sys.argv)
print (sys.argv[1:])
# ese "1:" es una nomenclatura de listas y tuplas
# sirgnifica "desde el elemento 1 en adelante", se salta el 0
#porque el elemento 0 de argv es el nombre del programa (igual que en C si se acuerdan)

# or it can be iterated via a for loop:

# el for cicla sobre todos los argumentos... hace un range(len(sys.argv))
# el len(sys.argv) les da la cantidad de argumentos
# la funcion len() es la que calcula la longitud de la lista
# range() genera un rango 0, 1, 2, .... hasta la cantidad de argumentos
# así, si tiene 4 argumentos, el for va a ciclar con 0, 1, 2 y 3

for i in range(len(sys.argv)):
    if i == 0:
        print("Function name: %s" % sys.argv[0])
    else:
        print ("%d. argument: %s" % (i,sys.argv[i]))

# acá importa sys
# luego usa sys.argv, que es una lista de los argumentos de la linea de comandos
#ejecutemos a ver...
