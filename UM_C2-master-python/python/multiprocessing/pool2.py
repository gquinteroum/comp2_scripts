#!/usr/bin/python

"""
    Pool of Workers
"""


from multiprocessing import Pool, TimeoutError
import time
import os
import random

def f(x):
    valor = random.randint(1,3)
    #time.sleep(valor)
    print("calculando %d (random: %d)" % (x,valor))
    return x*x

if __name__ == '__main__':
    pool = Pool(processes=4)              # start 4 worker processes

    input("Evaluamos la funcion f con los valores del 0 al 9:")
    print(pool.map(f, range(10)))
    # f(0), f(1), ... f(9)

    input("Hacemos lo mismo, pero de manera desordenada")
    for i in pool.imap_unordered(f, range(10)):
        print (i)

    input("Evaluamos f(20) de forma asincrónica y esperamos 1s de timeout")
    res = pool.apply_async(f, (20,))      # runs in *only* one process
    print(res.get(timeout=1))              # prints "400"

    input("Evaluamos el getpid de manera asincronica para un solo proceso")
    res = pool.apply_async(os.getpid, ()) # runs in *only* one process
    print (res.get(timeout=1))              # prints the PID of that process

    input("Hacemos lo mismo para varios procesos")
    multiple_results = [pool.apply_async(os.getpid, ()) for i in range(4)]
    print ([res.get(timeout=1) for res in multiple_results])
    
    """
    Version alternativa:
    multiple_results = []
    for i in range(4):
        multiple_results.append( pool.apply_async(os.getpid, ()) )

    for res in multiple_results:
        print(res.get(timeout=1))
    """

    input("Y ahora?")
    multiple_results = [pool.apply_async(os.getpid, ()) for i in range(10)]
    print ([res.get(timeout=1) for res in multiple_results])

    input("Dejamos a un solo worker esperando 10s pero al programa principal le damos un timeout de 1s:")
    res = pool.apply_async(time.sleep, (10,))
    try:
        print (res.get(timeout=1))
    except TimeoutError:
        print ("Hora de perder la paciencia y saltar con un multiprocessing.TimeoutError xD")
