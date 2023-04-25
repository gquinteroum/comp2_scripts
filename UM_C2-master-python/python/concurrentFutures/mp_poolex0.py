from concurrent.futures import ProcessPoolExecutor, wait, as_completed 
#import concurrent
from time import sleep
import os
import random

def return_after_n_secs( data ):
    message = data[0]
    n = data[1]
    sleep(n)
    print("Saliendo %d" % os.getpid())
    return message

def f1(pool, message, n):
    future = pool.submit(return_after_n_secs, (message, n))
    print(future.done())
    sleep(n+1)
    print(future.done())
    print(future.result())

def f2(pool, message, n):
    future1 = pool.submit(return_after_n_secs, (message,n))
    future2 = pool.submit(return_after_n_secs, (message+"_",n+2))
    print("Esperando...")
    sleep(1)
    print("Future1: "+str(future1))
    print("Future2: "+str(future2))
    print(future1.result())
    print("Future1: "+str(future1)+"\nFuture2: "+str(future2))
    print(future2.result())
    print("Future1: "+str(future1)+"\nFuture2: "+str(future2))

def f3(pool, n, a, b):
    futureses = []
    for i in range(n):
        s = random.randint(a, b)
        futureses.append(pool.submit(return_after_n_secs, ("Hola %d, esperando %d secs" % (i, s), s)))

    for i in as_completed(futureses):
        print("Resultado: %s" % i.result())
        print(futureses)

def f3wait(pool, n, a, b):
    futureses = []
    for i in range(n):
        s = random.randint(a, b)
        futureses.append(pool.submit(return_after_n_secs, ("Hola %d, esperando %d secs" % (i, s), s)))

    print("esperando...")
    wait(futureses)

    for i in futureses:
        print("Resultado: %s" % i.result())
        print(futureses)

def f4(pool, a, b):
    mensajes = ["hola", "mundo", "que", "tal", "como", "va", "todo"]
    data = []
    for m in mensajes:
        data.append((m,random.randint(a, b)))
        print(data[-1])
    resultado = pool.map(return_after_n_secs, data)

    # for i in as_completed(resultado):
        # print("Resultado: %s" % i.result())

    print(list(resultado))

if __name__=="__main__":
    pool = ProcessPoolExecutor()
    input("Veamos cuantos procs tenemos...")
    f1(pool, "holas", 6)
#    f2(pool, "holas", 3)
#    f3(pool, 3, 1, 4)
#    f3wait(pool, 3, 1, 4)
#    f4(pool, 1, 4)
    input("Veamos cuantos procs tenemos al final...")
