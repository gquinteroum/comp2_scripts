#!/usr/bin/python
import threading, time

f1 = threading.Semaphore(0)
f2 = threading.Semaphore(0)


def func1(n):
    for i in range(n):
        print("funcion1")
        time.sleep(1)
    f1.release() # semaforo f1 libera ejecucion
    f2.acquire() # semaforo f2 espera a que termine el otro
    print("finalizando1")


def func2(n):
    for i in range(n):
        print("funcion2")
        time.sleep(1)
    f2.release() # semaforo f2 libera ejecucion
    f1.acquire() # semaforo f1 espera a que termine el otro
    print("finalizando2")

if __name__ == "__main__":
    th = []
    th.append(threading.Thread(target=func1, args=(2,)))
    th[-1].start()
    th.append(threading.Thread(target=func2, args=(4,)))
    th[-1].start()
    
    for i in th:
        i.join()

