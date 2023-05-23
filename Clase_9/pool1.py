#!/usr/bin/python
from multiprocessing import Pool, Queue
import os
import signal
import time

def sumador(x):
    x = x+1

def pid(x):
    return ("pid: %d - x=%d" % (os.getpid(), x))

def cube(x):
    print("Proceso %d (padre: %d) calculando cubo de %d" %(os.getpid(),os.getppid(), x))
    time.sleep(1)
    return x**3

def cube_espera(x):
    print("Proceso %d (padre: %d) calculando cubo de %d" %(os.getpid(),os.getppid(), x))
    time.sleep(x)
    print("Calculo %d listo." % x)
    global cola
    cola.put(x**3)
    return x**3

def suma(a,b):
    print("Sumando %d con %d." % (a,b))
    return a+b


def map_():
    input("Antes que nada, abre otra terminal y ejecuta 'ps fax'... ¿que ves?")

    input("Pool.map simple")
    results = pool.map(cube, [3,4,5])
    print(results)

    input("Pool.map simple dos args")
    results = pool.starmap(suma, [[3,4],[6,7],[5,8]])
    print(results)

    # Ejecuta la funcion cube() con cada elemento de la lista
    # input("Pool.map")
    # results = pool.map(cube, range(15))
    # print(results)


def apply_():
    input("Pool.apply simple")
    results = pool.apply(cube, args=(3,))
    print(results)

    # Ejecuta la función cube() con un solo argumento
    input("Pool.apply")
    results = [pool.apply(cube, args=(x,)) for x in range(15)]
    print(results)

    input("Pool.apply again...")
    results=[]
    for x in range(15):
        results.append(pool.apply(cube,args=(x,)))
    print(results)

def mapapplyasync():
    input("Pool.map_async")
    results=[]
    results = pool.map_async(cube,range(15)).get()
    print("espereando...")
    print(results)

    """
    input("Pool.map_async separado")
    results=[]
    results = pool.map_async(cube,range(15))
    #asdfadfaf
    #asdfasdfasdf

    results = results.get()
    print("espereando...")
    print(results)
    """
    """
    input("Pool.apply async...")
    results=[]
    for x in range(15):
        results.append(pool.apply_async(cube,args=(x,)))

    print("espereando...")
    resultados = []
    for i in results:
        resultados.append(i.get())
    print(resultados)
    """

def orden():
    results=[]
    global cola
    for x in range(5,1,-1):
        results.append(pool.apply_async(cube_espera,args=(x,)))

    print("espereando...")
    resultados = []
    while True:
        print("resultados... ", cola.get())



def orden_imap():
    results=[]
    global cola
    for x in range(5,1,-1):
        results.append(pool.apply_async(cube_espera,args=(x,)))

    print("espereando...")
    resultados = []
    while True:
        print("resultados... ", cola.get())

cola = Queue()
pool = Pool(processes=4)
#results = pool.map(cube, [0,1,2,3,4,5,6])
#print(results)

# mapapplyasync()
map_()
