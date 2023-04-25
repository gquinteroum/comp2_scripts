import os, signal, sys
print(os.getpid())


def funcion(s,f):
    print("no me muero nada....")
    signal.signal(signal.SIGINT, signal.SIG_DFL)

# configuro el proc para que haga algo cuando reciba SIGINT
signal.signal(signal.SIGINT, funcion)

os.read(0,100)

