#!/usr/bin/python

#modulo getopt
import getopt
import sys

#getopt reconoce la entrada de linea de comandos y la parsea por nosotros

#funcion getopt del modulo getopt: getopt.getopt()
#sintaxis: getopt.getopt(argumentos, "opc_un_char" [, "opc_palabra"])
# getopt.getopt(sys.argv[1:], "abc", "hola")

#opciones validas: -a, -b -c

#(opt,arg) = getopt.getopt(sys.argv[1:], 'ab:c', ["hola", "mundo="])
# -a -b -c


#(opt,arg) = getopt.getopt(sys.argv[1:], 'ab:c')
# -a -b algo -c
# ./getopt.py -a -b 123 -c


#(opt,arg) = getopt.getopt(sys.argv[1:], 'a:b:c')
# -a algo -b algo -c


#(opt,arg) = getopt.getopt(sys.argv[1:], 'ab:c', ["opcion1", "opcion2"])
# -a -b algo -c --opcion1 --opcion2

#acá tienen un ejemplo de opciones cortas (-a, -b) y largas (--opcion1, --opcion2)

(opt,arg) = getopt.getopt(sys.argv[1:], 'ab:c', ["agregar", "opcion1", "opcion2="])
# -a -b algo -c --opcion1 --opcion2="holamundo"

#las que van con ":" como la b: son opciones que reciben argumentos, igual que en C
#el = en las opciones largas es equivalente al : en las cortas

print("opciones: ", opt)
print("argumentos: ", arg)

#parseamos los argumentos usando un for:

#ese for cicla por las opciones y va leyendo los argumentos si es que los tienen (-b debe tener, y --opcion2)
for (op,ar) in opt:
	if(op in ['-a', '--agregar']):
            print("Opcion -a o --agregar seteada")
	elif(op == '-b'):
		print("Opcion -b seteada, argumento: ", ar)
	elif(op == '-c'):
		print("Opcion -c seteada")
	elif(op == "--opcion1"):
		print("Opcion --opcion1 seteada")
	elif(op == "--opcion2"):
		print("Opcion --opcion2 seteada, argumento: ", ar)
	else:
		print("Opcion invalida")

#ese for cuando termina ya se ha parseado toda la línea de ordenes
# si es -a o --agregar muestra un mensaje
#si es -b muestra un mensaje, y muestra el argumento que acompaña a -b (por ejemplo, -b 123)
# si es -c hace lo mismo que con -a
# si es --opcion2 muestra un mensaje, y lee el argumento (ej, --opcion2=hola)

#ejecutemos para que lo vean
