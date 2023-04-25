from concurrent.futures import ThreadPoolExecutor, wait, as_completed
from time import sleep
from random import randint
 
def function(num):
    sleep(randint(1, 5))
    return "Return of %s" % format(num)
 

def con_ascomplete():
    pool = ThreadPoolExecutor(5)
    futures = []
    for x in range(5):
        futures.append(pool.submit(function, x))
     
    #vamos mostrando resultados ni bien salen del horno
    for x in as_completed(futures):
        print(x.result())

def con_wait():
    pool = ThreadPoolExecutor()
    futures = []
    for x in range(5):
        futures.append(pool.submit(function, x))

    #esperamos todos los resultados
    wait(futures)

    #mostramos (salen en orden)
    for x in futures:
        print(x.result())

print("Usando as_complete")
con_ascomplete()
print("Usando wait")
con_wait()
