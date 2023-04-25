import random, time
from threading import Event, Thread

"""
event por default es False
el wait lo pone a True, y es bloqueante
el set desbloquea al hilo que estaba esperando (no lo pone en falso)
el clear lo resetea, vuenve a False
"""

event = Event()

dato = 0

def cosumidor(event, nloops):
    for i in range(nloops):
        print("Esperando que esté disponible el dato...")
        event.wait() # Blocks until the flag becomes true.
        print("Dato disponible: ", dato)
        event.clear() # Resets the flag.

def productor(event, nloops):
    global dato
    for i in range(nloops):
        espera = random.randrange(2,5)
        print("Productor generando dato (%s s)" % espera)
        time.sleep(espera) # Sleeps for some time.
        dato = dato + 1
        event.set()

threads = []
nloops = random.randrange(3, 6)

threads.append(Thread(target=cosumidor, args=(event, nloops)))
threads[-1].start()
threads.append(Thread(target=productor, args=(event, nloops)))
threads[-1].start()

for thread in threads:
    thread.join()

print("All done.")
