
from multiprocessing import Process, Semaphore
import time

def f(l, n):
    l.acquire()
    for i in range(3):
        print ("hello world %d %d (Semaforo: %d)" % (n,i, l.get_value()))
        time.sleep(1)
    l.release()

if __name__ == '__main__':
    lock = Semaphore(2)
    procs=[]
    print("Valor inicial del semaforo: %d" % lock.get_value())

    for num in range(5):
        procs.append(Process(target=f, args=(lock, num)))
        procs[num].start()

    for num in range(5):
        procs[num].join()

    print("Valor final del semaforo: %d" % lock.get_value())

