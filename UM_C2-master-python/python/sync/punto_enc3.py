#!/usr/bin/python
import threading, time

barrera = threading.Barrier(3)

def func1(n):
    for i in range(n):
        print("funcion1")
        time.sleep(1)
    barrera.wait()
    print("finalizando1")


def func2(n):
    for i in range(n):
        print("funcion2")
        time.sleep(1)
    barrera.wait()
    print("finalizando2")

def func3(n):
    for i in range(n):
        print("funcion3")
        time.sleep(1)
    barrera.wait()
    print("finalizando3")


if __name__ == "__main__":
    th = []
    th.append(threading.Thread(target=func1, args=(2,)))
    th[-1].start()
    th.append(threading.Thread(target=func2, args=(4,)))
    th[-1].start()
    th.append(threading.Thread(target=func3, args=(6,)))
    th[-1].start()
    
    for i in th:
        i.join()

