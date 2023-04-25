
import threading
import time

def f(l, n):
    l.acquire()
    for i in range(3):
        print ("hello world %d %d" % (n,i))
        time.sleep(1)
    l.release()


def f_with(l, n):
    with l:
        for i in range(3):
            print ("hello world %d %d" % (n,i))
            time.sleep(1)


if __name__ == '__main__':
    semaforo = threading.BoundedSemaphore(1)

    for num in range(2):
        threading.Thread(target=f, args=(semaforo, num)).start()

#    for num in range(2):
#        threading.Thread(target=f_with, args=(semaforo, num)).start()
