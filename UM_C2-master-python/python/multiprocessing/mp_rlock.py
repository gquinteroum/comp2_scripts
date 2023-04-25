#rlock_tut.py
import multiprocessing



def lock():
    num = 0
    lock = multiprocessing.Lock()
    print("Bajando lock")
    lock.acquire()
    num += 1
    print("Bajando otra vez lock")
    lock.acquire() # This will block.
    num += 2
    lock.release()


# With RLock, that problem doesn't happen.
def rlock():
    num = 0
    lock = multiprocessing.RLock()

    print("Bajando rlock")
    lock.acquire()
    num += 3
    print("Bajando otra vez rlock")
    lock.acquire() # This won't block.
    num += 4
    lock.release()
    lock.release() # You need to call release once for each call to acquire.
    print(num)

if __name__ == "__main__":
    rlock()

"""
    Lock bloquea al proceso que llama al acquire ante de liberarlo con release.
    Rlock no bloquea al propio proceso

    Lock puede ser liberado por otro proceso, rlock solamente por el proceso

"""
