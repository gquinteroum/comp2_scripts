#!/usr/bin/python
import threading, time

f1_2 = threading.Semaphore(0)
f1_3 = threading.Semaphore(0)
f2_1 = threading.Semaphore(0)
f2_3 = threading.Semaphore(0)
f3_1 = threading.Semaphore(0)
f3_2 = threading.Semaphore(0)


def func1(n):
    for i in range(n):
        print("funcion1")
        time.sleep(1)
    f1_2.release()
    f1_3.release()
    f2_1.acquire()
    f3_1.acquire()
    print("finalizando1")


def func2(n):
    for i in range(n):
        print("funcion2")
        time.sleep(1)
    f2_1.release()
    f2_3.release()
    f1_2.acquire()
    f3_2.acquire()
    print("finalizando2")

def func3(n):
    for i in range(n):
        print("funcion3")
        time.sleep(1)
    f3_1.release()
    f3_2.release()
    f1_3.acquire()
    f2_3.acquire()
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

