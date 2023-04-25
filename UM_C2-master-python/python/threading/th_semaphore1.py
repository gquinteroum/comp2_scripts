import random, time
from threading import BoundedSemaphore, Thread
max_items = 5
"""
El container es un recipiente con una capacidad de max_items unidades
"""
container = BoundedSemaphore(max_items)

def producer(nloops):
    for i in range(nloops):
        time.sleep(random.randrange(2, 5))
        print(time.ctime(), end=": ")
        try:
            container.release()
            print("Produciendo un item.")
        except ValueError:
            print("Contenedor lleno!!.")

def consumer(nloops):
    for i in range(nloops):
        time.sleep(random.randrange(2, 5))
        print(time.ctime(), end=": ")
        """
        El false desactiva el bloqueo por defecto cuando el contenedor está vacío.
        """
        if container.acquire(False):
            print("Item consumido.")
        else:
            print("Vacío... saltando.")


threads = []
nloops = random.randrange(3, 6)
print("Iniciando con %s items." % max_items)
threads.append(Thread(target=producer, args=(nloops,)))
threads.append(Thread(target=consumer, args=(random.randrange(nloops, nloops+max_items+2),)))
for thread in threads:  # Starts all the threads.
    thread.start()
for thread in threads:  # Waits for threads to complete before moving on with the main script.
    thread.join()
print("All done.")
