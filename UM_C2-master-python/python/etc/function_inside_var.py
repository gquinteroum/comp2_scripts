import sys

def function_1():
    print("Holas")


def function_2():
    print("Mundos")


var = sys.argv[1]

# ejecución de la función cuyo nombre está guardado en la variable "var"
funcion_generica = eval(var)
funcion_generica()
