import threading, time

NTHREADS=5 # numero de threads
NITER=1000000 # numero de iteraciones

contador=0

def count(b, s):
    global contador
    for i in range(NITER):
        s.acquire()
        tmp = contador
        tmp = tmp+1
        for i in range(1):
            pass
        contador = tmp
        s.release()

#    b.wait()
    print("Hilo terminando: ", threading.current_thread().name)


barrera = threading.Barrier(NTHREADS)
sema = threading.Semaphore(1)

hilos = []
for i in range(NTHREADS):
    hilos.append(threading.Thread(target=count, args=(barrera,sema)))
    hilos[-1].start()


for i in range(NTHREADS):
    hilos[i].join()

if (contador != NTHREADS*NITER):
    print("NOOOOOO! contador es [%d] y deberia ser %d" % (contador, NITER*NTHREADS))
else:
    print("Bien!! contador vale %d" % contador)


