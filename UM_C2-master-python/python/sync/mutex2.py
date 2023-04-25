import threading
import time

num = 0

l = threading.Lock()
b = threading.Barrier(2)

def sumador(n):
    global num
    l.acquire()
    for i in range(n):
        if (num % 100000) == 0:
            print("sumando...")
        aux = num
        aux = aux+1
        num = aux
    l.release()
    b.wait()
    print("num en sumador vale: %d" % num)

def restador(n):
    global num
    l.acquire()
    for i in range(n):
        if (num % 100000) == 0:
            print("restando...")
        aux = num
        aux = aux-1
        num = aux
    l.release()

    b.wait()
    print("num en restador vale: %d" % num)

if __name__ == "__main__":
    th = []
    th.append(threading.Thread(target=sumador, args=(1000000,)))
    th[-1].start()
    th.append(threading.Thread(target=restador, args=(1000000,)))
    th[-1].start()
    
    for i in th:
        i.join()
