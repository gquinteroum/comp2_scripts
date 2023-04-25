import random, time
from threading import Event, Thread

event = Event()

def waiter(event, nloops):
    for i in range(nloops):
        print("%s. Esperando a que alguien setee el flag (Event: %s)." % (i+1, event.is_set()))
        event.wait() # Blocks until the flag becomes true.
        print("Wait completado %s (Event: %s):" % (time.ctime(), event.is_set()))
        event.clear() # Resets the flag.
        print("waiter final: ", event.is_set())

def setter(event, nloops):
    for i in range(nloops):
        time.sleep(random.randrange(2, 5)) # Sleeps for some time.
        event.set()

threads = []
nloops = random.randrange(3, 6)

threads.append(Thread(target=waiter, args=(event, nloops)))
threads[-1].start()
threads.append(Thread(target=setter, args=(event, nloops)))
threads[-1].start()

for thread in threads:
    thread.join()

print("All done.")
