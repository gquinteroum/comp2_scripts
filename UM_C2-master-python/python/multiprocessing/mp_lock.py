
from multiprocessing import Process, Lock
import os
import time

def f(l, n):
    print("Lanzando proceso: %d, PID %d" % (n, os.getpid()))
    l.acquire()
    for i in range(3):
        print ("hello world %d %d" % (n,i))
        time.sleep(1)
    l.release()

if __name__ == '__main__':
    lock = Lock()
    procs=[]

    for num in range(50):
        procs.append(Process(target=f, args=(lock, num)))
        procs[num].start()

    for num in range(50):
        procs[num].join()

